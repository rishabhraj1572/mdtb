from pyrogram import Client
from pyrogram import filters
import os
import threading
import mdisk
import split

bot_token = os.environ.get("TOKEN", "") 
api_hash = os.environ.get("HASH", "") 
api_id = os.environ.get("ID", "") 

app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)

TG_SPLIT_SIZE = 2097151000

@app.on_message(filters.command(["start"]))
def echo(client, message):
    app.send_message(message.chat.id, 'Send me the mdisk link like this >> /mdisk link')

'''async def progress(current, total):
    await app.send_message(message.chat.id,f"{current * 100 / total:.1f}%")'''

@app.on_message(filters.command(["mdisk"]))
def echo(client, message):
    try:
        link = message.text.split("mdisk ")[1]
        if "mdisk" in link:
            out = mdisk.req(link)
            app.send_message(message.chat.id, out)
    except:
        app.send_message(message.chat.id, 'send only mdisk link with command followed by link')


app.run()    
