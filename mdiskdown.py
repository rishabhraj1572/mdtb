from pyrogram import Client
from pyrogram import filters
import os
import threading
import mdisk
import split
import requests



bot_token = os.environ.get("TOKEN", "") 
api_hash = os.environ.get("HASH", "") 
api_id = os.environ.get("ID", "") 

app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)


@app.on_message(filters.command(["start"]))
def echo(client, message):
    app.send_message(message.chat.id, 'Send me the mdisk link like this >> /mdisk link')

'''async def progress(current, total):
    await app.send_message(message.chat.id,f"{current * 100 / total:.1f}%")'''


@app.on_message(filters.command(["mdisk"]))
def echo(client, message):
    try:
        inp = message.text.split("mdisk ")[1]
        fxl = inp.split("/")
        cid = fxl[-1]

        URL = f'https://diskuploader.entertainvideo.com/v1/file/cdnurl?param={cid}'

        header = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://mdisk.me/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
        }

        resp = requests.get(url=URL, headers=header).json()['source']
        out = resp
        app.send_message(message.chat.id, out)
    except:
        app.send_message(message.chat.id, 'send only mdisk link with command followed by link')

app.run()    
