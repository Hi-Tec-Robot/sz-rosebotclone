from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton

from lang import get_command
from button import formatting

from Rose import app
from Rose.utils.lang import language
from Rose.mongo.antiservice import (
    antiservice_on,
    antiservice_off,
    is_antiservice
)
from Rose.utils.filter_groups import service
from Rose.utils.custom_filters import can_change_filter


command = []
ANTI_SERV = get_command("ANTI_SERV")

@app.on_message(filters.command(ANTI_SERV) & can_change_filter)
@language
async def anti_service(client, message: Message, _):
    if len(message.command) != 2:
        return await message.reply_text(_["serv1"])
    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    chat_id = message.chat.id
    if status == "enable":
        await antiservice_on(chat_id)
        await message.reply_text(_["serv2"])
    elif status == "disable":
        await antiservice_off(chat_id)
        await message.reply_text(_["serv3"])
    else:
        await message.reply_text(_["serv1"])

@app.on_message(filters.service, group=service)
async def delete_service(_, message):
    chat_id = message.chat.id
    try:
        if await is_antiservice(chat_id):
            return 
    except Exception:
        pass
    

__MODULE__ = formatting
__HELP__ = f"""
**Formatting**
Rose supports a large number of formatting options to make
your messages more expressive. Take a look!
"""
__helpbtns__ = ([[InlineKeyboardButton('Markdown ', callback_data="_mdown"),InlineKeyboardButton('Fillings', callback_data='_fillings')],[InlineKeyboardButton('Random Content', callback_data="_random")]])
