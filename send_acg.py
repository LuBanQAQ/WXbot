import time
import requests
from utils import waiting_to_send, inWhiteList
last_sendacg_time = 0
waiting = 30   # 发送acg图片的等待时间
def sendACG(msg, wcf):
    if msg.from_group():
        if inWhiteList(msg.roomid):
            print("在白名单里")
            receiver = msg.roomid
        else:
            return
    else:
        receiver = msg.sender
    if msg.content == 'r18':
        if not waiting_to_send(waiting, last_sendacg_time):
            return
        wcf.send_text('你在想屁吃', receiver)
    elif msg.content == 'acg':
        if not waiting_to_send(waiting, last_sendacg_time):
            return
        wcf.send_image('https://api.miaomc.cn/image/get', receiver)
        print("发送了一张acg图片")
    elif msg.content.startswith("pic"):
        receiver = msg.sender
        if not waiting_to_send(waiting, last_sendacg_time):
            return
        parts = msg.content.split(" ", 1)
        if len(parts) > 1 and parts[1]:
            search_term = parts[1]
            json_url = f"https://api.lolicon.app/setu/v2?r18=0&tag={search_term}"
        else:
            json_url = "https://api.lolicon.app/setu/v2?r18=0"
        try:
            response = requests.get(json_url)
            response.raise_for_status()
            data = response.json().get("data", [])
            if not data:
                wcf.send_text("没有找到相关图片", receiver)
                print("No results found.")
            else:
                image_url = data[0].get("urls", {}).get("original")
                if image_url:
                    wcf.send_image(image_url, receiver)
                else:
                    print("Error: Invalid JSON response")
        except requests.RequestException as e:
            print(f"Network error: {e}")
        except ValueError as e:
            print(f"JSON decode error: {e}")