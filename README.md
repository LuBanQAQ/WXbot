# wxbot

这个项目是一个微信机器人，用于处理消息并执行诸如发送图片和拍一拍群成员等操作。

## 功能

- 接收并处理来自微信的消息。
- 根据特定消息发送图片。
- 在群聊中被提及时拍一拍群成员。

## 要求

- Python 3.x
- `wcferry` 库

## 安装

1. 克隆仓库：

    ```sh
    git clone https://github.com/LuBanQAQ/WXbot.git
    cd wxbot
    ```

3. 安装所需依赖：

    ```sh
    pip install wcferry pymysql
    ```

## 使用

1. 运行机器人：

    ```sh
    python main.py
    ```

## 代码概述

- `main.py`：初始化机器人并处理消息的主脚本。
- `client.py`：包含与微信交互的方法的 `Wcf` 类。

## 示例

要测试你的 `wxid` 获取函数是否正常工作，可以使用以下脚本：

```python
from wcferry import Wcf

# 初始化 Wcf 类
wcf = Wcf()

# 获取并打印你的 wxid
wxid = wcf.get_self_wxid()
print(f"我的 wxid 是: {wxid}")
