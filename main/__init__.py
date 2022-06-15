import asyncio
from main.utils.parser import auto_parser
from pyrogram import Client
from config import *
import libtorrent as lt


app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
  )

print("[INFO]: STARTING BOT...")
app.start()

print("[INFO]: STARTING Lib Torrent CLIENT")
ses = lt.session()
ses.listen_on(6881, 6891)

async def parsersss():
  print("Creating Parse task")
  asyncio.create_task(auto_parser())

asyncio.run(parsersss())