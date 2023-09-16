import asyncio
from datetime import datetime

import humanize
from pyrogram import filters, Client
from pyrogram.types import Message

from Tiger.helper.PyroHelpers import GetChatID, ReplyCheck
from Tiger.modules.help import add_command_help

AFK = False
AFK_REASON = ""
AFK_TIME = ""
USERS = {}
GROUPS = {}


def subtract_time(start, end):
    subtracted = humanize.naturaltime(start - end)
    return str(subtracted)


@Client.on_message(
    ((filters.group & filters.mentioned) | filters.private) & ~filters.me & ~filters.service, group=3
)
async def collect_afk_messages(bot: Client, message: Message):
    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME)
        is_group = True if message.chat.type in ["supergroup", "group"] else False
        CHAT_TYPE = GROUPS if is_group else USERS

        if GetChatID(message) not in CHAT_TYPE:
            text = (
                f"𝗜 𝗮𝗺 𝗻𝗼𝘁 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗿𝗶𝗴𝗵𝘁 𝗻𝗼𝘄...\n"
                f"𝗟𝗮𝘀𝘁 𝘀𝗲𝗲𝗻: {last_seen}\n"
                f"𝗥𝗲𝗮𝘀𝗼𝗻..: ```{AFK_REASON.upper()}```\n"

            )
            await bot.send_message(
                chat_id=GetChatID(message),
                text=text,
                reply_to_message_id=ReplyCheck(message),
            )
            CHAT_TYPE[GetChatID(message)] = 1
            return
        elif GetChatID(message) in CHAT_TYPE:
            if CHAT_TYPE[GetChatID(message)] == 50:
                text = (
                    f"𝗟𝗮𝘀𝘁 𝘀𝗲𝗲𝗻: {last_seen}\n"
                    f"𝗡𝗼 𝗺𝗼𝗿𝗲 𝗮𝘂𝘁𝗼 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗳𝗼𝗿 𝘆𝗼𝘂`"
                )
                await bot.send_message(
                    chat_id=GetChatID(message),
                    text=text,
                    reply_to_message_id=ReplyCheck(message),
                )
            elif CHAT_TYPE[GetChatID(message)] > 50:
                return
            elif CHAT_TYPE[GetChatID(message)] % 5 == 0:
                text = (
                    f"`𝗛𝗲𝘆 𝗜𝗺 𝘀𝘁𝗶𝗹𝗹 𝗻𝗼𝘁 𝗯𝗮𝗰𝗸 𝘆𝗲𝘁.\n"
                    f"𝗟𝗮𝘀𝘁 𝘀𝗲𝗲𝗻: {last_seen}\n"
                    f"𝗦𝘁𝗶𝗹𝗹 𝗯𝘂𝘀𝘆: ```{AFK_REASON.upper()}```\n"
                )
                await bot.send_message(
                    chat_id=GetChatID(message),
                    text=text,
                    reply_to_message_id=ReplyCheck(message),
                )

        CHAT_TYPE[GetChatID(message)] += 1


@Client.on_message(filters.command("afk", ".") & filters.me, group=3)
async def afk_set(bot: Client, message: Message):
    global AFK_REASON, AFK, AFK_TIME

    cmd = message.command
    afk_text = ""

    if len(cmd) > 1:
        afk_text = " ".join(cmd[1:])

    if isinstance(afk_text, str):
        AFK_REASON = afk_text

    AFK = True
    AFK_TIME = datetime.now()

    await message.delete()


@Client.on_message(filters.command("afk", "!") & filters.me, group=3)
async def afk_unset(bot: Client, message: Message):
    global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME).replace("ago", "").strip()
        await message.edit(
            f"`𝗪𝗵𝗶𝗹𝗲 𝘆𝗼𝘂 𝘄𝗲𝗿𝗲 𝗮𝘄𝗮𝘆 (for {last_seen}), 𝘆𝗼𝘂 𝗿𝗲𝗰𝗲𝗶𝘃𝗲𝗱 {sum(USERS.values()) + sum(GROUPS.values())} "
            f"𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗳𝗿𝗼𝗺 {len(USERS) + len(GROUPS)} 𝗰𝗵𝗮𝘁𝘀`"
        )
        AFK = False
        AFK_TIME = ""
        AFK_REASON = ""
        USERS = {}
        GROUPS = {}
        await asyncio.sleep(5)

    await message.delete()

if AFK:
   @Client.on_message(filters.me, group=3)
   async def auto_afk_unset(bot: Client, message: Message):
       global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

       if AFK:
           last_seen = subtract_time(datetime.now(), AFK_TIME).replace("ago", "").strip()
           reply = await message.reply(
               f"`𝗪𝗵𝗶𝗹𝗲 𝘆𝗼𝘂 𝘄𝗲𝗿𝗲 𝗮𝘄𝗮𝘆 (for {last_seen}), 𝘆𝗼𝘂 𝗿𝗲𝗰𝗲𝗶𝘃𝗲𝗱 {sum(USERS.values()) + sum(GROUPS.values())} "
               f"𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗳𝗿𝗼𝗺 {len(USERS) + len(GROUPS)} chats`"
           )
           AFK = False
           AFK_TIME = ""
           AFK_REASON = ""
           USERS = {}
           GROUPS = {}
           await asyncio.sleep(5)
           await reply.delete()


add_command_help(
    "afk",
    [
        [".afk", "𝗔𝗰𝘁𝗶𝘃𝗮𝘁𝗲𝘀 𝗔𝗙𝗞 𝗺𝗼𝗱𝗲 𝘄𝗶𝘁𝗵 𝗿𝗲𝗮𝘀𝗼𝗻 𝗮𝘀 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗮𝗳𝘁𝗲𝗿 .𝗮𝗳𝗸\𝗻𝗨𝘀𝗮𝗴𝗲: ```.𝗮𝗳𝗸 <𝗿𝗲𝗮𝘀𝗼𝗻>```"],
        ["!afk", "𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲𝘀 𝗔𝗙𝗞 𝗺𝗼𝗱𝗲."],
    ],
)      
