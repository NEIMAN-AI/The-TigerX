import os
from asyncio import sleep
import os
import sys
from re import sub
from time import time


from pyrogram import Client, filters, enums
from pyrogram.types import Message

from Tiger import SUDO_USER
from Tiger.helper.PyroHelpers import ReplyCheck

from Tiger.modules.help import add_command_help

flood = {}
profile_photo = "kidzz/pfp.jpg"


async def extract_userid(message, text: str):
    def is_int(text: str):
        try:
            int(text)
        except ValueError:
            return False
        return True

    text = text.strip()

    if is_int(text):
        return int(text)

    entities = message.entities
    app = message._client
    if len(entities) < 2:
        return (await app.get_users(text)).id
    entity = entities[1]
    if entity.type == "mention":
        return (await app.get_users(text)).id
    if entity.type == "text_mention":
        return entity.user.id
    return None


async def extract_user_and_reason(message, sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    if message.reply_to_message:
        reply = message.reply_to_message
        if not reply.from_user:
            if (
                reply.sender_chat
                and reply.sender_chat != message.chat.id
                and sender_chat
            ):
                id_ = reply.sender_chat.id
            else:
                return None, None
        else:
            id_ = reply.from_user.id

        if len(args) < 2:
            reason = None
        else:
            reason = text.split(None, 1)[1]
        return id_, reason

    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await extract_userid(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await extract_userid(message, user), reason

    return user, reason


async def extract_user(message):
    return (await extract_user_and_reason(message))[0]

@Client.on_message(
    filters.command(["unblock"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴... . . .`")
    if not user_id:
        return await message.edit(
            "𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗨𝘀𝗲𝗿 𝗜𝗗/𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝗼𝗿 𝗿𝗲𝗽𝗹𝘆 𝘁𝗼 𝘂𝘀𝗲𝗿 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘁𝗼 𝘂𝗻𝗯𝗹𝗼𝗰𝗸."
        )
    if user_id == client.me.id:
        return await tex.edit("𝗽𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴....")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗨𝗻𝗯𝗹𝗼𝗰𝗸𝗲𝗱** {umention}")

@Client.on_message(
    filters.command(["block"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    tex = await message.reply_text("`𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴... . . .`")
    if not user_id:
        return await tex.edit_text(
            "𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗨𝘀𝗲𝗿 𝗜𝗗/𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝗼𝗿 𝗿𝗲𝗽𝗹𝘆 𝘁𝗼 𝘂𝘀𝗲𝗿 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘁𝗼 𝗯𝗹𝗼𝗰𝗸."
        )
    if user_id == client.me.id:
        return await tex.edit_text("ohk ✅.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit_text(f"**𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗯𝗹𝗼𝗰𝗸𝗲𝗱** {umention}")


@Client.on_message(
    filters.command(["setname"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def setname(client: Client, message: Message):
    tex = await message.reply_text("`𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴.. . . .`")
    if len(message.command) == 1:
        return await tex.edit(
            "𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝘁𝗲𝘅𝘁 𝘁𝗼 𝘀𝗲𝘁 𝗮𝘀 𝘆𝗼𝘂𝗿 𝗻𝗮𝗺𝗲."
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(f"**𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗖𝗵𝗮𝗻𝗴𝗲𝗱 𝗬𝗼𝘂𝗿 𝗡𝗮𝗺𝗲 𝗧𝗼** `{name}`")
        except Exception as e:
            await tex.edit(f"**ERROR:** `{e}`")
    else:
        return await tex.edit(
            "𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝘁𝗲𝘅𝘁 𝘁𝗼 𝘀𝗲𝘁 𝗮𝘀 𝘆𝗼𝘂𝗿 𝗻𝗮𝗺𝗲."
        )

@Client.on_message(
    filters.command(["setbio"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def set_bio(client: Client, message: Message):
    tex = await message.edit_text("`𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴.. . . .`")
    if len(message.command) == 1:
        return await tex.edit("𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝘁𝗲𝘅𝘁 𝘁𝗼 𝘀𝗲𝘁 𝗮𝘀 𝗯𝗶𝗼.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"**𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗖𝗵𝗮𝗻𝗴𝗲 𝘆𝗼𝘂𝗿 𝗕𝗜𝗢 𝘁𝗼** `{bio}`")
        except Exception as e:
            await tex.edit(f"**ERROR:** `{e}`")
    else:
        return await tex.edit("𝗣𝗿𝗼𝘃𝗶𝗱𝗲 𝘁𝗲𝘅𝘁 𝘁𝗼 𝘀𝗲𝘁 𝗮𝘀 𝗯𝗶𝗼.")


@Client.on_message(
    filters.command(["setpfp"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.reply_text("**𝗬𝗼𝘂𝗿 𝗣𝗿𝗼𝗳𝗶𝗹𝗲 𝗣𝗵𝗼𝘁𝗼 𝗖𝗵𝗮𝗻𝗴𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆.**")
    else:
        await message.reply_text(
            "𝗥𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮𝗻𝘆 𝗽𝗵𝗼𝘁𝗼 𝘁𝗼 𝘀𝗲𝘁 𝗮𝘀 𝗽𝗿𝗼𝗳𝗶𝗹𝗲 𝗽𝗵𝗼𝘁𝗼"
        )
        await sleep(3)
        await message.delete()


@Client.on_message(
    filters.command(["vpfp"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def view_pfp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id:
        user = await client.get_users(user_id)
    else:
        user = await client.get_me()
    if not user.photo:
        await message.reply_text("𝗣𝗿𝗼𝗳𝗶𝗹𝗲 𝗽𝗵𝗼𝘁𝗼 𝗻𝗼𝘁 𝗳𝗼𝘂𝗻𝗱!")
        return
    await client.download_media(user.photo.big_file_id, file_name=profile_photo)
    await client.send_photo(
        message.chat.id, profile_photo, reply_to_message_id=ReplyCheck(message)
    )
    await message.delete()
    if os.path.exists(profile_photo):
        os.remove(profile_photo)


add_command_help(
    "profile",
    [
        ["block", "𝘁𝗼 𝗯𝗹𝗼𝗰𝗸 𝘀𝗼𝗺𝗲𝗼𝗻𝗲 𝗼𝗻 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺"],
        ["unblock", "𝘁𝗼 𝘂𝗻𝗯𝗹𝗼𝗰𝗸 𝘀𝗼𝗺𝗲𝗼𝗻𝗲 𝗼𝗻 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺"],
        ["setname", "𝘀𝗲𝘁 𝘆𝗼𝘂𝗿 𝗽𝗿𝗼𝗳𝗶𝗹𝗲 𝗻𝗮𝗺𝗲."],
        ["setbio", "𝘀𝗲𝘁 𝗮𝗻 𝗯𝗶𝗼."],
        [
            "setpfp",
            f"𝗿𝗲𝗽𝗹𝘆 𝘄𝗶𝘁𝗵 𝗶𝗺𝗮𝗴𝗲 𝘁𝗼 𝘀𝗲𝘁 𝘆𝗼𝘂𝗿 𝗽𝗿𝗼𝗳𝗶𝗹𝗲 𝗽𝗶𝗰.",
        ],
        ["vpfp", "𝗥𝗲𝗽𝗹𝘆 𝘄𝗶𝘁𝗵 𝘃𝗶𝗱𝗲𝗼 𝘁𝗼 𝘀𝗲𝘁 𝘆𝗼𝘂𝗿 𝘃𝗶𝗱𝗲𝗼 𝗽𝗿𝗼𝗳𝗶𝗹𝗲."],
    ],
)
