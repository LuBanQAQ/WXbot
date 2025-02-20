from queue import Empty
from threading import Thread
from wcferry import Wcf, WxMsg
from motd_utils import motd, motdbe
from send_acg import sendACG
from send_img import sendIMG
from utils import inWhiteList, addWhiteList
from openai_client import sendGPT

wcf = Wcf()
last_sendacg_time = [0]  # 使用列表来传递引用
waiting = 30   # 发送acg图片的等待时间
admin = 'wxid_xxx' # 管理员的wxid
api_key = "xxx" # OpenAI的API Key

def processMsg(msg: WxMsg):
    if msg.from_group():
        print(f"群聊{msg.roomid}收到群消息来自{msg.sender}: {msg.content} {msg.id}")
    else:
        print(f"来自{msg.sender}收到个人消息: {msg.content} {msg.id}")

def testMsg(msg: WxMsg):
    if msg.from_group():
        receiver = msg.roomid
    else:
        receiver = msg.sender
    if msg.content == "1":
        if msg.from_group() and inWhiteList(msg.roomid):
            wcf.send_text("test", receiver)
            wcf.send_image('https://motdbe.blackbe.work/status_img?host=play.easecation.net:19132', receiver)
            print(wcf.get_msg())
            print("发送了一条测试消息")

def enableReceivingMsg():
    def innerWcFerryProcessMsg():
        while wcf.get_msg_types:
            try:
                msg = wcf.get_msg()
                processMsg(msg)
                sendIMG(msg, wcf)
                sendACG(msg, wcf)
                sendGPT(msg, wcf, api_key, last_sendacg_time, waiting)
                # testMsg(msg)
                addWhiteList(msg, admin, wcf)
                motd(msg, wcf)
                motdbe(msg, wcf)
            except Empty:
                continue
            except Exception as e:
                print(f"错误: {e}")

    print("启动消息监听...")
    wcf.enable_receiving_msg()
    Thread(target=innerWcFerryProcessMsg, name="ListenMessageThread", daemon=True).start()

enableReceivingMsg()
wcf.keep_running()