import os
import jmcomic
from jmcomic import JmOption
from utils import waiting_to_send, inWhiteList
last_sendacg_time = 0
waiting = 10
def download_jmcomic(album_id):
    option_path = os.path.abspath('./option.yml')
    yml = jmcomic.create_option_by_file(option_path)
    jmcomic.download_album(album_id, yml)
def sendJM(msg,wcf):
    if msg.from_group():
        if inWhiteList(msg.roomid):
            # print("在白名单里")
            receiver = msg.sender
        else:
            return
    else:
        receiver = msg.sender
    if msg.content.startswith("jm"):
        parts = msg.content.split(" ")
        album_id = parts[1]
        if not waiting_to_send(waiting, last_sendacg_time):
            return
        wcf.send_text("Downloading...", receiver)
        download_jmcomic(album_id)

        pdf_path = f"D:\\pdf\\{album_id}.pdf"
        if os.path.isfile(pdf_path):
            result = wcf.send_image(pdf_path, receiver)
            if result != 0:
                wcf.send_text("Failed to send PDF.", receiver)
        else:
            wcf.send_text("PDF not found.", receiver)