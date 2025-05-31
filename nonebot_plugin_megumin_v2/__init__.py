from nonebot import get_driver, require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_uninfo")
require("nonebot_plugin_alconna")
require("nonebot_plugin_localstore")

from .config import PluginConfig, plugin_config
from .magic import *


__plugin_meta__ = PluginMetadata(
    name="为美好群聊献上爆炎2",
    description="现在，你的群友可以触发失传已久的爆裂魔法了！ ",
    usage=get_help(),
    type="application",
    homepage="https://github.com/youlanan/nonebot_plugin_megumin",
    config=PluginConfig,
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_uninfo",
        "nonebot_plugin_alconna",
        "nonebot_plugin_localstore"
    )
)


from pathlib import Path
from nonebot.log import logger
import urllib.request
import asyncio
import zipfile

driver = get_driver()

@driver.on_startup
async def check_and_download_resources():
    """资源初始化入口（异步安全版）"""
    target_dir = plugin_config.megumin_res_dir
    marker = target_dir / ".explosion2"
    
    # 创建目标目录（自动处理权限）
    target_dir.mkdir(parents=True, exist_ok=True)
    
    if marker.exists():
        logger.info("✔ 爆炎资源已就绪")
        return

    logger.warning("⚠ 正在初始化爆裂魔法资源...")
    await async_downloader(
        url="https://github.proxy.class3.fun/https://github.com/youlanan/nonebot_plugin_megumin/releases/download/v0.2.0/Explosion_2.zip",
        target_dir=target_dir,
        marker_file=marker,
        max_retries=2,
        retry_delay=5
    )

async def async_downloader(
    url: str,
    target_dir: Path,
    marker_file: Path,
    max_retries: int = 3,
    retry_delay: int = 5
) -> bool:
    """异步安全下载器"""
    file_name = Path(url).name
    temp_file = target_dir / f"~{file_name}.tmp"
    is_zip = file_name.lower().endswith('.zip')

    for attempt in range(1, max_retries + 1):
        try:
            # 清理残留临时文件
            if temp_file.exists():
                temp_file.unlink()

            # 在独立线程中执行阻塞操作
            success = await asyncio.to_thread(
                _sync_download,
                url, temp_file, target_dir
            )
            
            if success:
                # 处理压缩文件
                if is_zip:
                    final_file = target_dir / file_name
                    with zipfile.ZipFile(final_file, 'r') as zf:
                        zf.extractall(target_dir)
                    final_file.unlink()
                
                # 创建成功标记
                marker_file.touch()
                logger.success("✔ 资源部署完成")
                return True

        except Exception as e:
            logger.error(f"✘ 尝试 {attempt}/{max_retries} 失败: {e}")
            if attempt < max_retries:
                logger.info(f"⌛ {retry_delay}秒后重试...")
                await asyncio.sleep(retry_delay)
            continue
    
    logger.critical("✘ 资源初始化失败，部分功能受限")
    logger.info(f"请手动下载: {url}\n解压至: {target_dir}")
    return False

def _sync_download(url: str, temp_path: Path, target_dir: Path) -> bool:
    """同步下载核心（带基础校验）"""
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        
        with urllib.request.urlopen(req, timeout=15) as response:
            # 获取基础信息
            total_size = int(response.headers.get('Content-Length', 0))
            logger.debug(f"文件尺寸: {total_size // 1024}KB")

            # 进度跟踪
            downloaded = 0
            last_percent = -1
            
            with temp_path.open('wb') as f:
                while True:
                    chunk = response.read(4096)
                    if not chunk:
                        break
                    
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    # 进度提示（仅整10%）
                    if total_size > 0:
                        percent = (downloaded * 100) // total_size
                        if percent != last_percent and percent % 10 == 0:
                            logger.info(f"▷ 进度: {percent}%")
                            last_percent = percent
            
            # 基础完整性检查
            if total_size > 0 and downloaded != total_size:
                raise IOError("文件不完整")
                
            # 重命名临时文件
            final_path = target_dir / Path(url).name
            temp_path.rename(final_path)
            return True

    except Exception as e:
        if temp_path.exists():
            temp_path.unlink(missing_ok=True)
        raise
