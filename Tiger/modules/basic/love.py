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

@Client.on_message(filters.command(["love", "love"], ".") & filters.me)
async def hearts(client: Client, message: Message):
    await phase1(message)
    await asyncio.sleep(SLEEP * 3)
    await message.edit(" ▄▀▄▀")
    await asyncio.sleep(0.5)
    await message.edit("▄▀▄▀▄▀▄")
    await asyncio.sleep(0.5)
    await message.edit("▄▀▄▀▄▀▄▀▄▀")
    await asyncio.sleep(0.5)
    await message.edit("▄▀▄▀▄▀▄▀▄▀▄▀▄")
    await asyncio.sleep(0.5)
    await message.edit("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄")
    await asyncio.sleep(0.5)
    await message.edit("𝗝𝗔𝗬 ▄▀▄▀▄▀▄▀▄▀")
    await asyncio.sleep(0.5)
    await message.edit("𝗝𝗔𝗬 𝗦𝗛𝗥𝗘𝗘 ▀▄▀▄▀▄▀")
    await asyncio.sleep(0.5)
    await message.edit("𝗝𝗔𝗬 𝗦𝗛𝗥𝗘𝗘 𝗥𝗔𝗠 🚩🚩▀▄▀")
    await asyncio.sleep(3)
    await message.edit("𝗝𝗔𝗬 𝗦𝗛𝗥𝗘𝗘 𝗥𝗔𝗠 🚩🚩🔥")

add_command_help(
    "love",
    [
        [".love", "𝗨𝗦𝗘 𝗔𝗡𝗗 𝗞𝗡𝗢𝗪"],
    ],
  )
