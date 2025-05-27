<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/youlanan/nonebot_plugin_megumin/blob/main/img/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot_plugin_megumin

_✨ 为美好群聊献上爆炎 ✨_


<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

<details>
<summary>【点此查看插件 v1 版本的介绍】</summary>

---

## 🌱 介绍

_可以触发 以视频、或语音+文字 形式的爆裂魔法_

_自带刷屏屏蔽、可自定义释放与补魔次数_

_让群友领略最强魔法的艺术与魅力_

_爆裂魔法啦啦啦(⑅ōᴗō)۶..._

## 🔧 安装

**如果你认为旧版本插件更符合需求，请手动克隆项目到本地使用**

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-megumin

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-megumin
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_megumin"]

</details>

<details>
<summary>下载源码安装</summary>

    下载仓库源码后, 将 nonebot_plugin_megumin 丢进nb目录下的src/plugin目录下, 确保已正确配置nb可以载入该目录内的插件

</details>

- 需要发送视频或语音, 所以请确保你安装并正确配置了ffmpeg
- 完成上述步骤后，下载项目' 爆炎资源包 '中的' Explosion.zip ', 按提示将资源放置在指定位置, 以完成安装
- 可供选择的触发形式为视频/语音/混合, 在项目的' cfg.py '文件中进行修改, 有对应注释说明

## ✨ 指令
### 指令表
| 指令 | 权限 | 指令前缀 | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 爆裂魔法 | 群员 | 默认 | 群聊 | 常用触发指令 |
| 补魔 | 群员 | 默认 | 群聊私聊 | 刷新可触发次数 |
| 补魔帮助 | 群员 | 默认 | 群聊私聊 | 插件的帮助 |

---
</details>


## 🌱 介绍

_可以触发 以视频、或语音+文字 形式的爆裂魔法_

_可自定义玩家每日补魔极限与释放次数_

_让群友领略最强魔法的浪漫_

_(⑅ōᴗō)۶エクスプロージョン！..._

<details>
<summary>更新说明</summary>

相比v1版本：

v2适配了QQ适配器（得益于跨平台的nonebot-plugin-uninfo和plugin-alconna，或许其他平台也能用）

v2取消了刷屏检测（因为消息去重或防刷屏应该是某个全局性插件要做的事，比如指令阻断）

v2新增了日语和更多配置项（详见 安装-配置项 部分）

v2新增了自动下载资源（包含某些平台专用的silk格式，如不需要可手动删除）

</details>

## 🔧 安装

（如果你认为旧版本插件更符合需求，请手动克隆项目与对应资源到本地使用）

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-megumin

</details>

<details>
<summary>使用pip安装</summary>

    pip install nonebot-plugin-megumin

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_megumin"]

</details>

<details>
<summary>下载源码安装</summary>

- 下载仓库源码后

- 将 nonebot_plugin_megumin 丢进nb目录下的src/plugin目录下

- 确保已正确配置nb可以载入该目录内的插件

</details>

- 需要发送视频或语音, 所以请确保你安装并正确配置了ffmpeg

<details>
  
<summary>v2配置项（可忽略）</summary>

## 配置项

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

</details>

## ✨ 指令
### 指令表
| 指令 | 权限 | 指令前缀 | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 爆裂魔法帮助  explosion help | 群员 | 默认 | 群聊私聊 | 插件的帮助 |
| 爆裂魔法  explosion | 群员 | 默认 | 群聊私聊 | 常用触发指令 |
| 补魔  replenish | 群员 | 默认 | 群聊私聊 | 刷新可触发次数 |

注：如果给bot配置过指令前缀, 则触发指令为前缀+指令, 例如 /爆裂魔法
### 效果图
<img src="https://github.com/youlanan/nonebot_plugin_megumin/blob/main/img/help.png" width="300" height="700" alt="效果图">
<img src="https://github.com/youlanan/nonebot_plugin_megumin/blob/main/img/q.jpg" width="300" height="500" alt="茶话会">

## ⚡ 项目灵感
>伊雷娜bot曾经有的功能

>[借鉴了EXPLOSION-惠惠爆裂魔法语音](https://github.com/pcrbot/Explosion)

_（本人纯小白一枚, 如果感觉代码很乱或者出现各种问题纯属正常, 欢迎反馈纠错~）_
