import time
import schedule
from threading import Thread
from utils import inWhiteList
from main import wcf
groupList = ['48652991926@chatroom']

def sendNotice():
    for group in groupList:
        wcf.send_text("定时发送测试信息1", "48652991926@chatroom")
def schedule_send_notice():
    while True:
        current_time = time.strftime("%H:%M")
        # Replace with desired times
        if current_time == "09:00" or current_time == "22:43":
            print("Sending notice...")
            sendNotice()
            # Perform your sending logic here
            time.sleep(60)
        time.sleep(1)

# Start the scheduler in a separate thread without arguments
Thread(target=schedule_send_notice, name="SchedulerThread", daemon=True).start()