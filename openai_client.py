import os
import time
from openai import OpenAI
from utils import waiting_to_send, inWhiteList

def sendGPT(msg, wcf, api_key, last_sendacg_time, waiting):
    if msg.from_group():
        if inWhiteList(msg.roomid):
            receiver = msg.roomid
        else:
            return
    else:
        receiver = msg.sender

    if msg.content.startswith("gpt "):
        if not waiting_to_send(waiting, last_sendacg_time[0]):
            return
        prompt = msg.content[4:]
        try:
            client = OpenAI(
                api_key=api_key,
                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            )

            completion = client.chat.completions.create(
                model="qwen-plus",
                messages=[
                    {'role': 'system', 'content': 'You are a helpful assistant.'},
                    {'role': 'user', 'content': prompt}
                ]
            )
            response = completion.choices[0].message.content
            wcf.send_text(response, receiver)
            last_sendacg_time[0] = time.time()  # 更新上次发送时间
        except Exception as e:
            error_message = f"错误信息：{e}\n请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code"
            wcf.send_text(error_message, receiver)