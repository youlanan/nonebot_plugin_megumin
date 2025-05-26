from pathlib import Path
from pydantic import BaseModel
from nonebot import get_plugin_config
import nonebot_plugin_localstore as store

class PluginConfig(BaseModel):

    megumin_send_mode: int = 0
    '''发送模式（群聊）: 0为先视频后语音+文本、1为纯视频、2纯语音、3为文本+语音、4为随机'''

    megumin_private_send_mode: int = 3
    '''发送模式（私信、非群聊）: 同上、0为禁用、4为纯文本'''

    megumin_max_cast: int = 2
    '''释法次数（设置单玩家魔力满值时可以释放几次）: 为0时使用无限制、最低为1'''

    megumin_max_recover: int = 2
    '''补魔次数（设置每日允许玩家回复几次魔力）: 为0时使用无限制、最低为1'''

    megumin_res_dir: Path = store.get_plugin_data_dir()
    '''资源路径: （未指定时，默认使用本地数据储存插件提供的路径）'''

    megumin_language: str = "zh"
    '''显示语言: zh: 中文、ja: 日文'''

plugin_config = get_plugin_config(PluginConfig)
