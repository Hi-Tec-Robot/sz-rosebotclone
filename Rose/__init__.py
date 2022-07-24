import os
import time
import pymongo
import asyncio

from aiohttp import ClientSession
from inspect import getfullargspec

from Python_ARQ import ARQ
from motor.motor_asyncio import AsyncIOMotorClient

from pyrogram import Client, ContinuePropagation
from pyrogram.types import Message
from pyrogram.errors import FloodWait

from config import *


SUPPORT_GROUP = "https://t.me/Infinity_Bot_Support"
SUDOERS = 1377217980
LOG_GROUP_ID = -1001511567994
MOD_LOAD = []
MOD_NOLOAD = []
bot_start_time = time.time()
DB_URI = BASE_DB 
MONGO_URL = MONGO_URL
OWNER_ID = 1377217980

myclient = pymongo.MongoClient(DB_URI)
dbn = myclient["supun"]

mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client.wbb

loop = asyncio.get_event_loop()

aiohttpsession = ClientSession()

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

bot = Client("supun", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
app = Client("app2", bot_token=BOT_TOKEN, api_id=API_ID1, api_hash=API_HASH1)

BOT_ID = 0
BOT_NAME = ""
BOT_USERNAME = ""
BOT_MENTION = ""
BOT_DC_ID = 0

async def initiate_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION, BOT_DC_ID
    os.system("clear")
    print(" ************** START DEPLOYING ************** ")
    print(" _____________________________________________")
    print("|          Isabella - Base Pyrogram           |")
    print("|     Most Advanced Group Management Bot      |")
    print("|---------------------------------------------|")
    print("|         (C) 2022 by @DarkRider2003          |")
    print("|    Support Chat is @Infinity_Bot_Support    |")
    print("\_____________________________________________/")
    
    try:
        print("\n┌ Starting Bot Client...")
        await bot.start()
        await app.start()
        print("└ Started Bot Client...")
        
        await asyncio.sleep(0.5)
    except FloodWait as f:
        await asyncio.sleep(f.x)
        raise ContinuePropagation
    
    try:
        print("\n┌ Loading Bot Information...")
        x = await app.get_me()
        
        BOT_ID = int(x.id)
        BOT_NAME = str((x.first_name + " " + x.last_name) if (x.last_name) else (x.first_name))
        BOT_USERNAME = str(x.username)
        BOT_MENTION = x.mention
        BOT_DC_ID = int(x.dc_id)
        
        print("└ Loaded Bot Information...")
        
        await asyncio.sleep(1)
    except FloodWait as f:
        await asyncio.sleep(f.x)
        raise ContinuePropagation


async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})

loop.run_until_complete(initiate_bot())
