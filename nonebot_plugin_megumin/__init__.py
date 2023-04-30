from nonebot.adapters.onebot.v11 import GroupMessageEvent, GROUP, MessageSegment
from nonebot import get_driver, on_command
from nonebot.log import logger
from pathlib import Path
from .charm import *
from .cfg import *
import asyncio
import random
import time

driver = get_driver()


@driver.on_startup
def 魔法文件们():
    主目录 = Path.cwd()
    魔法目录 = 主目录.joinpath("data/explosion")

    if not 魔法目录.exists():
        logger.info(f"\033[31m 没有找到配置目录 {魔法目录} ")

    AAC = list(魔法目录.glob("*.aac"))
    if not AAC:
        logger.info(f"\033[31m 配置目录 {魔法目录} 中没有音频文件 ")

    MP4 = list(魔法目录.glob("*.mp4"))
    if not MP4:
        logger.info(f"\033[31m 配置目录 {魔法目录} 中没有视频文件 ")


玩家吟唱 = {}
补魔次数 = {}
视频次数 = {}
无魔防刷屏 = {}

ex = on_command("爆裂魔法",
                aliases={"惠惠", "explosion", "来一发", "爆烈魔法", "暴烈魔法", "献上爆炎"},
                permission=GROUP,
                priority=90)


@ex.handle()
async def 施法(event: GroupMessageEvent):
    玩家 = event.user_id
    群 = event.group_id
    今天 = await 时间()

    if 玩家吟唱.get(玩家, {}).get(今天, 0) >= 释放极限:
        if 无魔防刷屏.get(玩家, {}).get(今天, 0) >= 6:
            return
        if 补魔次数.get(玩家, {}).get(今天, 0) >= 补魔极限:
            await ex.send("你今天已经施展过了，下次再来吧~")
            无魔防刷屏.setdefault(玩家, {})
            无魔防刷屏[玩家][今天] = 无魔防刷屏[玩家].get(今天, 0) + 1
            return
        await ex.send(f"你今天已经释放{释放极限}次了，请恢复魔力后再来吧~")
        无魔防刷屏.setdefault(玩家, {})
        无魔防刷屏[玩家][今天] = 无魔防刷屏[玩家].get(今天, 0) + 1
        return

    if 混合发送 == 2:
        if 视频次数.get(群, {}).get(今天, 0) >= 1:
            await 语音(玩家, 今天)
            return
        await 视频(玩家, 今天)
        视频次数.setdefault(群, {})
        视频次数[群][今天] = 视频次数[群].get(今天, 0) + 1
    elif 混合发送 == 1:
        await 视频(玩家, 今天)
    else:
        await 语音(玩家, 今天)


async def 视频(玩家, 今天):
    魔法阵 = random.choice(高端吟唱体验)

    主目录 = Path.cwd()
    魔法目录 = 主目录.joinpath("data/explosion")
    绝对魔力 = Path.cwd() / 魔法目录 / 魔法阵
    绝对魔力.resolve()

    施法 = MessageSegment.video(f"file:///{str(绝对魔力)}")
    await ex.send(施法)

    玩家吟唱.setdefault(玩家, {})
    玩家吟唱[玩家][今天] = 玩家吟唱[玩家].get(今天, 0) + 1
    logger.info(f"\033[32m 玩家 {玩家} 施展了一次视频爆裂魔法 ")


async def 语音(玩家, 今天):
    条目 = random.choice(list(吟唱词.keys()))
    魔咒 = 吟唱词[条目]

    主目录 = Path.cwd()
    魔法目录 = 主目录.joinpath("data/explosion")
    绝对魔力 = Path.cwd() / 魔法目录 / 条目
    绝对魔力.resolve()

    吟唱 = MessageSegment.record(f"file:///{str(绝对魔力)}")
    await ex.send(吟唱)
    await asyncio.sleep(0.5)  # 防风措施
    await ex.send(魔咒)

    玩家吟唱.setdefault(玩家, {})
    玩家吟唱[玩家][今天] = 玩家吟唱[玩家].get(今天, 0) + 1
    logger.info(f"\033[32m 玩家 {玩家} 施展了一次语音爆裂魔法 ")


exp = on_command("补魔", aliases={"补充魔力", "恢复魔力"}, priority=90)


@exp.handle()
async def 恢复(event: GroupMessageEvent):
    玩家 = event.user_id

    今天 = await 时间()

    if 补魔次数.get(玩家, {}).get(今天, 0) >= 补魔极限:
        await ex.send(f"你今天已经补魔{补魔极限}次了，明天再继续吧~")
        return

    玩家吟唱.setdefault(玩家, {})
    玩家吟唱[玩家][今天] = 0

    await exp.send(f"解锁成就：再来{释放极限}发！")

    补魔次数.setdefault(玩家, {})
    补魔次数[玩家][今天] = 补魔次数[玩家].get(今天, 0) + 1
    logger.info(f"\033[32m 玩家 {玩家} 为自己补魔 ")


async def 时间():
    日期 = time.localtime(time.time())
    return time.strftime("%Y-%m-%d", 日期)


exhelp = on_command("爆裂魔法帮助", aliases={"爆裂魔法help", "补魔帮助"}, priority=90)


@exhelp.handle()
async def 帮助(event: GroupMessageEvent):
    玩家 = event.user_id
    今天 = await 时间()
    if 无魔防刷屏.get(玩家, {}).get(今天, 0) >= 6:
        return
    await exp.send(
        f"吾名惠惠！\n乃浪漫炽热【爆裂魔法】支配者\n每日{释放极限}发的惊人力量！\n以{补魔极限}次【补魔】引渡魔力本源！\n为你之群聊献上爆炎！\n『Explosion！』\n\n详细介绍：https://github.com/youlanan/nonebot_plugin_megumin"
    )
    无魔防刷屏.setdefault(玩家, {})
    无魔防刷屏[玩家][今天] = 无魔防刷屏[玩家].get(今天, 0) + 1
