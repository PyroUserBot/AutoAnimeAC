from config import CHANNEL_ID
from pyrogram.types import Message
from main.modules.progress import progress_for_pyrogram
from os.path import isfile
import os
import time
from main import app

async def upload_video(msg: Message,file):
    fuk = isfile(file)
    if fuk:
        r = msg
        c_time = time.time()
        z = await app.send_video(
            CHANNEL_ID,
        video=file,
        caption=os.path.basename(file),
        progress=progress_for_pyrogram,
        progress_args=(
            os.path.basename(file),
            r,
            c_time
        )
        )
        os.remove(file)
    
    try:
        await r.delete()
        os.remove(file)
    except:
        pass
    return