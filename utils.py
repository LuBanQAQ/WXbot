import os
import requests
import time

def download_image(url, file_name, save_dir=None):
    if save_dir is None:
        save_dir = os.path.dirname(__file__)
    save_path = os.path.join(save_dir, file_name)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check if the request was successful
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded and saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")

def waiting_to_send(wait_duration: int, last_sendacg_time: float):
    current_time = time.time()
    if current_time - last_sendacg_time < wait_duration:
        print(f"等待 {int(wait_duration - (current_time - last_sendacg_time))} 秒.")
        return False
    return True

def inWhiteList(roomid, whitelist_path='whitelist.txt'):
    with open(whitelist_path, 'r') as f:
        for line in f:
            if roomid in line:
                return True
    return False

def addWhiteList(msg, admin, wcf, whitelist_path='whitelist.txt'):
    if msg.sender == admin and msg.content == 'add':
        if inWhiteList(msg.roomid, whitelist_path):
            wcf.send_text("已在白名单里", msg.roomid)
        else:
            with open(whitelist_path, 'a') as f:
                f.write(msg.roomid + '\n')
            wcf.send_text("已添加群聊白名单", msg.roomid)

    elif msg.sender == admin and msg.content == 'del':
        if inWhiteList(msg.roomid, whitelist_path):
            with open(whitelist_path, 'r') as f:
                lines = f.readlines()
            with open(whitelist_path, 'w') as f:
                for roomid in lines:
                    if roomid.strip('\n') != msg.roomid:
                        f.write(roomid)
            wcf.send_text("已删除群聊白名单", msg.roomid)
        else:
            wcf.send_text("不在白名单里", msg.roomid)