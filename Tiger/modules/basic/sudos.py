from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
DEVS = int(6358121681)
from Tiger.helper.PyroHelpers import get_ub_chats
from Tiger.modules.basic.profile import extract_user, extract_user_and_reason
from Tiger import SUDO_USER
from config import OWNER_ID
from Tiger.modules.help import add_command_help

ok = []


@Client.on_message(filters.command("sudolist", ".") & filters.me)
async def gbanlist(client: Client, message: Message):
    users = (SUDO_USER)
    ex = await message.edit_text("`𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴....`")
    if not users:
        return await ex.edit("𝗡𝗼 𝗨𝘀𝗲𝗿𝘀 𝗵𝗮𝘃𝗲 𝗯𝗲𝗲𝗻 𝘀𝗲𝘁 𝘆𝗲𝘁")
    gban_list = "**Sudo Users:**\n"
    count = 0
    for i in users:
        count += 1
        gban_list += f"**{count} -** `{i}`\n"
    return await ex.edit(gban_list)


@Client.on_message(filters.command("addsudo", ".") & filters.user(OWNER_ID))
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.reply_text("`𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴....`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗽𝗲𝗰𝗶𝗳𝘆 𝗮 𝘃𝗮𝗹𝗶𝗱 𝘂𝘀𝗲𝗿!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗽𝗲𝗰𝗶𝗳𝘆 𝗮 𝘃𝗮𝗹𝗶𝗱 𝘂𝘀𝗲𝗿!`")
        return
    if user.id == client.me.id:
        return await ex.edit("**𝗢𝗸𝗮𝘆 𝗯𝗮𝗯𝗲...**")

    try:
        if user.id in SUDO_USER:
            return await ex.edit("`𝗨𝘀𝗲𝗿 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗶𝗻 𝘀𝘂𝗱𝗼`")
        SUDO_USER.append(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) 𝗔𝗱𝗱𝗲𝗱 𝗧𝗼 𝗦𝘂𝗱𝗼 𝗨𝘀𝗲𝗿𝘀!")
    
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("rmsudo", ".") & filters.user(OWNER_ID))
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.reply_text("`𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴....`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗽𝗲𝗰𝗶𝗳𝘆 𝗮 𝘃𝗮𝗹𝗶𝗱 𝘂𝘀𝗲𝗿!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗽𝗲𝗰𝗶𝗳𝘆 𝗮 𝘃𝗮𝗹𝗶𝗱 𝘂𝘀𝗲𝗿!`")
        return
    if user.id == client.me.id:
        return await ex.edit("**O𝗸𝗮𝘆 𝗯𝗮𝗯𝗲...**")

    try:
        if user.id not in SUDO_USER:
            return await ex.edit("`𝗨𝘀𝗲𝗿 𝗶𝘀 𝗻𝗼𝘁 𝗮 𝗽𝗮𝗿𝘁 𝗼𝗳 𝘀𝘂𝗱𝗼`")
        SUDO_USER.remove(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) 𝗥𝗲𝗺𝗼𝘃𝗲𝗱 𝗧𝗼 𝗦𝘂𝗱𝗼 𝗨𝘀𝗲𝗿𝘀!")
    
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return



add_command_help(
    "sudos",
    [
        [
            "addsudo <reply/username/userid>",
            "𝗔𝗱𝗱 𝗮𝗻𝘆 𝘂𝘀𝗲𝗿 𝗮𝘀 𝗦𝘂𝗱𝗼 (𝗨𝘀𝗲 𝗧𝗵𝗶𝘀 𝗔𝘁 𝘆𝗼𝘂𝗿).",
        ],
        ["rmsudo <reply/username/userid>", "𝗥𝗲𝗺𝗼𝘃𝗲 𝗦𝘂𝗱𝗼 𝗮𝗰𝗰𝗲𝘀𝘀."],
        ["sudolist", "𝗗𝗶𝘀𝗽𝗹𝗮𝘆𝘀 𝘁𝗵𝗲 𝗦𝘂𝗱𝗼 𝗟𝗶𝘀𝘁."],
    ],
)
