from time import time
import asyncio
from pyrogram.types import Message
from Rose.utils.extract_user import extract_user
from Rose import BOT_ID,app
from Rose.utils.functions import extract_user_and_reason,time_converter
from pyrogram.types import Message
from lang import get_command
from Rose.utils.commands import *
from Rose.utils.lang import *
from Rose.utils.custom_filters import restrict_filter
from Rose.plugins.fsub import ForceSub
from button import *

@app.on_message(command(gban) )
@language
async def gbanFunc(client, message: Message, _):
    reason = None
    if len(message.text.split()) >= 2:
        reason = message.text.split(None, 1)[1]
    try:
        await message.chat.gban_member(message.from_user.id)
        txt = f" Bye {message.from_user.mention}, you're right - get out."
        txt += f"\n<b>Reason</b>: {reason}" if reason else ""
        await message.reply_text(txt)
        await message.chat.unban_member(message.from_user.id)
    except Exception as ef:
        await message.reply_text(f"{ef}")
    return
                {
                    "_id": user_id,
                    "reason": reason,
                    "by": by_user,
                    "time": time_rn,
                },
            )
