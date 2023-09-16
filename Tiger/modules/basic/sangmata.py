import asyncio

from pyrogram import *
from pyrogram import filters
from pyrogram.errors import YouBlockedUser
from pyrogram.types import *


from Tiger.modules.help import add_command_help
from Tiger.modules.basic.profile import extract_user

@Client.on_message(filters.command(["sg", "sa", "sangmata"], ".") & filters.me)
async def sg(client: Client, message: Message):
    args = await extract_user(message)
    lol = await message.edit_text("`𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            return await lol.edit(f"`𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗽𝗲𝗰𝗶𝗳𝘆 𝗮 𝘃𝗮𝗹𝗶𝗱 𝘂𝘀𝗲𝗿!`")
    bot = "SangMata_beta_bot"
    try:
        await client.send_message(bot, f"/{user.id}")
    except YouBlockedUser:
        await client.unblock_user(bot)
        await client.send_message(bot, f"{user.id}")
    await asyncio.sleep(1)

    async for stalk in client.search_messages(bot, query="Name", limit=1):
        if not stalk:
            await message.edit_text("**𝗢𝗿𝗮𝗻𝗴 𝗜𝗻𝗶 𝗕𝗲𝗹𝘂𝗺 𝗣𝗲𝗿𝗻𝗮𝗵 𝗠𝗲𝗻𝗴𝗴𝗮𝗻𝘁𝗶 𝗡𝗮𝗺𝗮𝗻𝘆𝗮**")
            return
        elif stalk:
            await message.edit(stalk.text)
            await stalk.delete()

    async for stalk in client.search_messages(bot, query="Username", limit=1):
        if not stalk:
            return
        elif stalk:
            await message.reply(stalk.text)
            await stalk.delete()


add_command_help(
    "sangmata",
    [
        [
            "sg [reply/userid/username]",
            "𝗜𝘁𝘀 𝗵𝗲𝗹𝗽 𝘂𝗵 𝘁𝗼 𝗳𝗶𝗻𝗱 𝘀𝗼𝗺𝗲𝗼𝗻𝗲 𝗻𝗮𝗺𝗲 𝗵𝗶𝘀𝘁𝗼𝗿𝘆.",
        ],
    ],
)
                                  
