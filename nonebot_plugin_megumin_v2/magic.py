from nonebot.log import logger
from nonebot_plugin_alconna import on_alconna, Alconna, Option
from nonebot_plugin_alconna.uniseg import UniMessage, Voice, Audio, Video, Text
from nonebot_plugin_uninfo import Uninfo

from .charm import get_random_entry, get_i18n_tips
from .config import plugin_config
from .state import Limit

from pathlib import Path
import random
import sys


class 歪比巴卜:
    mode = plugin_config.megumin_send_mode
    pmode = plugin_config.megumin_private_send_mode
    res_dir = plugin_config.megumin_res_dir
    language = plugin_config.megumin_language
    max_cast = "∞" if plugin_config.megumin_max_cast == 0 else plugin_config.megumin_max_cast
    max_recover = "∞" if plugin_config.megumin_max_recover == 0 else plugin_config.megumin_max_recover


施法 = on_alconna(
    Alconna("explosion", Option("help|帮助")),
    aliases={"爆炎", "爆裂魔法", "来一发", "惠惠", "爆烈魔法", "Explosion"},
    auto_send_output=True
)

@施法.assign("help")
async def _():
    await 施法.finish(UniMessage(get_help()))

def get_help():
    """获取帮助信息"""
    return get_i18n_tips("help", 歪比巴卜.language).format(歪比巴卜.max_recover, 歪比巴卜.max_cast)

@施法.handle()
async def _(session: Uninfo):
    user_id = session.user.id
    if Limit.no_can_spells(user_id):
        logger.opt(colors=True).info(f"<yellow> 玩家 {user_id} 爆炎次数已达上限 </yellow>")
        await 施法.finish(get_i18n_tips("吟唱上限", 歪比巴卜.language))

    is_group = session.scene.type.name == "GROUP"
    mode = 歪比巴卜.mode if is_group else 歪比巴卜.pmode

    if not is_group and mode == 0:
        logger.opt(colors=True).info(f"<yellow> 玩家 {user_id} 试图在 被禁用的私信 中施展爆炎 </yellow>")
        return

    scope = str(session.scope)
    scene_id = session.scene.id if is_group else None
    msg = await case_mode(mode, scope, scene_id)
    if isinstance(msg, list):
        for i in msg:
            await 施法.send(i)
    else:
        await 施法.finish(msg)


补魔 = on_alconna(
    Alconna("replenish"),
    aliases={"补魔", "补充魔力", "恢复魔力", "补充魔法", "恢复魔法"},
    auto_send_output=True
)

@补魔.handle()
async def _(session: Uninfo):
    userid = session.user.id
    if Limit.no_can_recover(userid):
        logger.opt(colors=True).info(f"<yellow> 玩家 {userid} 今日补魔次数已上限 </yellow>")
        await 补魔.finish(get_i18n_tips("补魔上限", 歪比巴卜.language).format(歪比巴卜.max_recover))
    logger.opt(colors=True).info(f"<yellow> 玩家 {userid} 为自己补魔 </yellow>")
    await 补魔.finish(get_i18n_tips("补魔成功", 歪比巴卜.language).format(歪比巴卜.max_cast))


async def case_mode(
    mode: int, 
    scope: str, 
    groupid: str | None
    ):
    """
    发送模式（群聊）: 0为先视频后语音+文本、1为纯视频、2纯语音、3为语音+文本、4为随机
    发送模式（私信）: 同上、0为禁用、4为纯文本
    """
    mode = random.randint(1, 4) if mode == 4 else mode
    key, txt = get_random_entry(歪比巴卜.language)
    if sys.version_info >= (3, 10):
        match mode:
            case 0 if groupid:
                if Limit.allow_video(groupid):
                    return send_video(key)
                return send_voice_text(key, txt, scope)
            case 1:
                return send_video(key)
            case 2:
                return send_voice(key, scope)
            case 3:
                return send_voice_text(key, txt, scope)
            case 4:
                return send_text(key, txt, scope)
            case _:
                return UniMessage("ModeErr")
    else:
        if mode == 0 and groupid:
            if Limit.allow_video(groupid):
                return send_video(key)
            return send_voice_text(key, res, scope)
        elif mode == 1:
            return send_video(key)
        elif mode == 2:
            return send_voice(key, scope)
        elif mode == 3:
            return send_voice_text(key, res, scope)
        elif mode == 4:
            return send_text(key, res, scope)
        else:
            return UniMessage("ModeErr")

def send_video(key: str) -> UniMessage:
    '''发送视频'''
    logger.opt(colors=True).info("<yellow> 本次 Explosion 将发送视频 mp4 </yellow>")
    vi = 歪比巴卜.res_dir / "mp4" / f"{key}.mp4"
    if not Path(vi).exists():
        logger.warning(f"视频资源缺失: {vi}")
        return UniMessage(Text(f"（视频资源缺失）"))
    return UniMessage(Video(path=str(vi)))

def send_voice(key: str, scope: str) -> UniMessage:
    '''发送语音'''
    if scope == "QQAPI":
        logger.opt(colors=True).info("<yellow> 本次 Explosion 将发送语音 silk </yellow>")
        vo = 歪比巴卜.res_dir / "silk" / f"{key}.silk"
    else:
        logger.opt(colors=True).info("<yellow> 本次 Explosion 将发送语音 aac </yellow>")
        vo = 歪比巴卜.res_dir / "aac" / f"{key}.aac"
    if not Path(vo).exists():
        logger.warning(f"语音资源缺失: {vo}")
        return UniMessage(Text(f"（语音资源缺失）"))
    return UniMessage(Voice(path=str(vo)))

def send_text(key: str, txt: str, scope: str) -> UniMessage:
    '''发送文本'''
    logger.opt(colors=True).info(f"<yellow> 本次 Explosion 将发送文本 {key} to {scope} </yellow>")
    if scope == "QQAPI":
        return UniMessage(f"\n{txt}")
    return UniMessage(txt)

def send_voice_text(key: str, res: dict, scope: str) -> list:
    '''发送语音、文本'''
    return [send_text(key, res, scope), send_voice(key, scope)]
    # ✘send_text(key, res, scope) + send_voice(key, scope)
    # ✘MessageSegment(send_voice(key, scope), send_text(key, res, scope))
