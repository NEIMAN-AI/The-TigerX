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
    " нєуα му мαѕтєя⚡!\n\nιм уσυя ᴀssɪsᴛᴀɴᴛт?\n\n‣ ι ᴄᴀɴи нєℓρ уσυ тσ нσѕт уσυя ℓєfт ¢ℓιєитѕ.\n\n‣ яєρσ: github.com/NEIMAN-AI/The-TigerX \n\n‣ тнιѕ ѕρє¢ιαℓℓу fσя вυzzу ρєσρℓє\n\n‣ иσω /clone {ѕєи∂ уσυя ρуяσgяαм ѕтяιиg ѕєѕѕισи}"
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
    text = await msg.reply("υѕαgє:\n\n /clone ѕєѕѕισи")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("вσσтιиg уσυя ¢ℓιєит")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Tiger/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"уσυя ¢ℓιєит нαѕ вєєи ѕυ¢¢єѕѕfυℓℓу ѕтαят αѕ {user.first_name} ✅.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nρяєѕѕ /start тσ ѕтαят αgαιи.")
