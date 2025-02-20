import os
import random

def sendIMG(msg, wcf):
    if msg.from_group():
        receiver = msg.roomid
    else:
        receiver = msg.sender
    if msg.is_at(wcf.get_self_wxid()) or msg.content == "msz":
        script_dir = os.path.dirname(__file__)
        image_paths = [os.path.join(script_dir, 'img1.jpg'), os.path.join(script_dir, 'img2.jpg')]
        image_path = random.choice(image_paths)
        wcf.send_image(image_path, receiver)
        wcf.send_pat_msg(receiver, msg.sender)