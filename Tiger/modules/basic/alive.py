import asyncio
import random

import requests
from pyrogram import *
from pyrogram import Client, filters
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *
from pyrogram.types import Message


from Tiger.helper.basic import edit_or_reply, get_text
from Tiger.helper.constants import MEMES

from Tiger.modules.help import *


@Client.on_message(filters.command("alive", ".") & filters.me)
async def hello_world(client: Client, message: Message):
    mg = await edit_or_reply(
        message,
        "⚡𝗧𝗶𝗴𝗲𝗿𝗫 𝗜𝘀 𝗢𝗻𝗹𝗶𝗻𝗲⚡\n╔═══❰𝗧𝗵𝗲-𝗧𝗶𝗴𝗲𝗿𝗫❱═══╗\n┣⪼ ᴜᴘᴛɪᴍᴇ »`{uptime}`\n┣⪼ ᴘɪɴɢ » `%sms`\n┣⪼ 𝖳𝗂𝗀𝖾𝗋𝖷 »  {client.me.mention}\n╚══════════════╝"
)
