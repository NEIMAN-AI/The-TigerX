import os
import sys
import asyncio
import re
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from kidzz.data import *
from Tiger.database.rraid import *
from Tiger import SUDO_USER
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
DEVS = int(6358121681)
from Tiger.helper.PyroHelpers import get_ub_chats
from Tiger.modules.basic.profile import extract_user, extract_user_and_reason
SUDO_USERS = SUDO_USER
from .replyraid import RAIDS



@Client.on_message(
    filters.command(["replyraid"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴....`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗽𝗲𝗰𝗶𝗳𝘆 𝗮 𝘃𝗮𝗹𝗶𝗱 𝘂𝘀𝗲𝗿 𝗯𝗮𝗯𝗲...!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗽𝗲𝗰𝗶𝗳𝘆 𝗮 𝘃𝗮𝗹𝗶𝗱 𝘂𝘀𝗲𝗿 𝗯𝗮𝗯𝗲...!`")
        return
    if user.id == client.me.id:
        return await ex.edit("**𝗢𝗸𝗮𝘆 𝗯𝗮𝗯𝗲.. **")
    elif user.id == SUDO_USERS:
        return await ex.edit("**𝗢𝗸𝗮𝘆 𝗕𝘂𝘁 𝗙𝗮𝗶𝗹𝗲𝗱 𝗕𝗲𝗰𝗮𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝘂𝘀𝗲𝗿 𝗶𝗻 𝘀𝘂𝗱𝗼𝘀 𝗯𝗮𝗯𝗲. .. **")
    elif user.id == VERIFIED_USERS:
        return await ex.edit("**𝗖𝗵𝗮𝗹 𝗖𝗵𝗮𝗹 𝗕𝗮𝗮𝗽 𝗸𝗼 𝗠𝗮𝘁 𝘀𝗶𝗸𝗵𝗮...**")
    try:
        if user.id in (await get_rraid_users()):
           await ex.edit("𝗥𝗲𝗽𝗹𝘆𝗿𝗮𝗶𝗱 𝗶𝘀 𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲𝗱 𝗼𝗻 𝘁𝗵𝗶𝘀 𝘂𝘀𝗲𝗿 𝗯𝗮𝗯𝗲...")
           return
        await rraid_user(user.id)
        RAIDS.append(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) 𝗔𝗰𝘁𝗶𝘃𝗮𝘁𝗲𝗱 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱 𝗯𝗮𝗯𝗲...!")
    except Exception as e:
        await ex.edit(f"**𝗘𝗥𝗥𝗢𝗥:** `{e}`")
        return 
