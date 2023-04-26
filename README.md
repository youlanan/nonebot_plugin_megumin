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


## 🌱 介绍

_可以触发 以视频、或语音+文字 形式的爆裂魔法_

_自带刷屏屏蔽、可自定义释放与补魔次数_

_让群友领略最强魔法的艺术与魅力_

_爆裂魔法啦啦啦(⑅ōᴗō)۶..._

## 🔧 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot_plugin_megumin

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot_plugin_megumin
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_megumin"]

</details>

<details>
<summary>下载 本仓库源码 安装</summary>

    下载后将 nonebot_plugin_megumin 丢进nb目录下的src/plugin目录下, 确保正确配置nb可以载入该目录内的插件

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

注：如果给bot配置过指令前缀, 则触发指令为前缀+指令, 例如 /爆裂魔法
### 效果图
<img src="https://github.com/youlanan/nonebot_plugin_megumin/blob/main/img/help.png" width="300" height="700" alt="效果图">

## ⚡ 项目灵感
>伊雷娜bot曾经有的功能

>[借鉴了EXPLOSION-惠惠爆裂魔法语音](https://github.com/pcrbot/Explosion)
