import os
import requests
from utils import download_image, inWhiteList

def motd(msg, wcf):
    if msg.from_group():
        if inWhiteList(msg.roomid):
            receiver = msg.roomid
        else:
            return
    else:
        receiver = msg.sender
    if msg.content.startswith("motd "):
        parts = msg.content.split(" ", 1)
        if len(parts) > 1 and parts[1]:
            server_ip = parts[1]
            if ":" not in server_ip:
                server_ip += ":25565"
            motd_url = f"https://motdbe.blackbe.work/status_img/java?host={server_ip}"
            try:
                script_dir = os.path.dirname(__file__)
                image_paths = os.path.join(script_dir, 'java.png')
                download_image(motd_url, "java.png")
                if os.path.exists(image_paths):
                    wcf.send_image(image_paths, receiver)
                    os.remove(image_paths)
                else:
                    wcf.send_text("无法获取服务器信息", receiver)
            except requests.exceptions.RequestException as e:
                wcf.send_text(f"请求错误: {e}", receiver)

def motdbe(msg, wcf):
    if msg.from_group():
        if inWhiteList(msg.roomid):
            receiver = msg.roomid
        else:
            return
    else:
        receiver = msg.sender
    if msg.content.startswith("motdbe "):
        parts = msg.content.split(" ", 1)
        if len(parts) > 1 and parts[1]:
            server_ip = parts[1]
            if ":" not in server_ip:
                server_ip += ":19132"
            motd_url = f"https://motdbe.blackbe.work/status_img?host={server_ip}"
            try:
                dir = os.path.dirname(__file__)
                image_paths = os.path.join(dir, 'mcbe.png')
                download_image(motd_url, "mcbe.png")
                if os.path.exists(image_paths):
                    wcf.send_image(image_paths, receiver)
                    os.remove(image_paths)
                else:
                    wcf.send_text("无法获取服务器信息", receiver)
            except requests.exceptions.RequestException as e:
                wcf.send_text(f"请求错误: {e}", receiver)