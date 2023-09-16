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
        "╭✠╼━━━❰𝗧𝗵𝗲-𝗧𝗶𝗴𝗲𝗿𝗫❱━━━✠╮\n│» 𝗮𝗳𝗸\n│» 𝗺𝘂𝘀𝗶𝗰\n│» 𝗹𝘆𝗿𝗶𝗰𝘀\n│» 𝗴𝗼𝗼𝗴𝗹𝗲\n│» 𝗰𝗹𝗼𝗻𝗲\n│» 𝘀𝗽𝗮𝗺\n│» 𝗽𝗶𝗻𝗴\n│» 𝗮𝗹𝗶𝘃𝗲\n│» 𝘀𝘁𝗶𝗰𝗸𝗲𝗿𝘀\n│» 𝘀𝗮𝗻𝗴𝗺𝗲𝘁𝗮\n│» 𝗽𝗿𝗼𝗳𝗶𝗹𝗲\n│» 𝘁𝗲𝘅𝘁\n│» 𝗲𝗺𝗼𝗷𝗶\n│» 𝗱𝗺𝘀𝗽𝗮𝗺\n│» 𝘁𝗮𝗴𝗮𝗹𝗹\n│» 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗽𝗵\n│» 𝘃𝗰 𝘁𝗼𝗼𝗹𝘀\n│» 𝗷𝗼𝗶𝗻\n│» 𝗹𝗲𝗮𝘃𝗲\n│» 𝗜𝗻𝘃𝗶𝘁𝗲\n╰✠╼━━━━━━❖━━━━━━━✠╯"
    )
