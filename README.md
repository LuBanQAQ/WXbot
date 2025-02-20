# wxbot

这个项目是一个微信机器人，用于处理消息并执行诸如发送图片和拍一拍群成员等操作。

## 功能

- 接收并处理来自微信的消息。
- 根据特定消息发送图片。
- 在群聊中被提及时拍一拍群成员。
- 发送 Minecraft 服务器状态图片。
- 发送 OpenAI GPT 模型的回复。

## 要求

- Python 3.x
-  [wcferry](https://github.com/lich0821/WeChatFerry)库

## 安装

1. 克隆仓库：

    ```sh
    git clone https://github.com/LuBanQAQ/WXbot.git
    cd wxbot

2. 安装所需依赖：

    ```sh
    pip install wcferry
    ```

## 使用

1. 运行机器人：

    ```sh
    python main.py
    ```

## 代码概述

- `main.py`：初始化机器人并处理消息的主脚本。
- `client.py`：包含与微信交互的方法的 `Wcf` 类。
- `send_img.py`：根据特定消息发送图片。
- `send_acg.py`：根据特定消息发送 ACG 图片。
- `motd_utils.py`：发送 Minecraft 服务器状态图片。
- `openai_client.py`：发送 OpenAI GPT 模型的回复。
- `utils.py`：包含下载图片和管理白名单等工具函数。
- 

## 使用的API

- motd:https://github.com/BlackBEDevelopment/MCBE-Server-Motd
- setu:https://api.lolicon.app/

## 示例

要测试你的 `wxid` 获取函数是否正常工作，可以使用以下脚本：

```python
from wcferry import Wcf

# 初始化 Wcf 类
wcf = Wcf()

# 获取并打印你的 wxid
wxid = wcf.get_self_wxid()
print(f"我的 wxid 是: {wxid}")
```
