from Tiger import app, API_ID, API_HASH
from config import OWNER_ID, ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    " 𝗻𝗼𝘄 /clone {𝘀𝗲𝗻𝗱 𝘆𝗼𝘂𝗿 𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻}"
)

@app.on_message(filters.user(OWNER_ID) & filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("⚡𝘜𝘱𝘥𝘢𝘵𝘦𝘴 𝘤𝘩𝘢𝘯𝘯𝘦𝘭⚡", url="t.me/DETECTED_09"),
            ],
            [
                InlineKeyboardButton("⚡𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘎𝘳𝘰𝘶𝘱⚡", url="t.me/The_Tiger_X"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By Itz-Zaid Your motherfucker if uh Don't gives credits.
@app.on_message(filters.user(OWNER_ID) & filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("𝘂𝘀𝗮𝗴𝗲є:\n\n /clone 𝘀𝗲𝘀𝘀𝗶𝗼𝗻")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴....")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Tiger/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"𝘆𝗼𝘂𝗿 𝗖𝗹𝗶𝗲𝗻𝘁 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗗𝗲𝗽𝗹𝗼𝘆𝗲𝗱 𝗯𝗮𝗯𝗲...{user.first_name} ✅.")
    except Exception as e:
        await msg.reply(f"**𝗘𝗥𝗥𝗢𝗥:** `{str(e)}`\nρяєѕѕ /start 𝘁𝗼 𝘀𝘁𝗮𝗿𝘁 𝗮𝗴𝗮𝗶𝗻...")
