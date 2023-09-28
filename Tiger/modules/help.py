import asyncio

from prettytable import PrettyTable
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from Tiger import app, CMD_HELP
from Tiger.helper.PyroHelpers import ReplyCheck
from Tiger.helper.utility import split_list


async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    xyz = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await xyz(*args, **kwargs)

@Client.on_message(filters.command(["help", "helpme"], ".") & filters.me)
async def module_help(client: Client, message: Message):
    mg = await edit_or_reply(
        message,
        "╭✠╼━━━❰𝗧𝗵𝗲-𝗧𝗶𝗴𝗲𝗿𝗫❱━━━✠╮\n\n\n [here](@DETECTED_09)"
    )
