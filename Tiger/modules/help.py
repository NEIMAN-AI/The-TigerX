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
            return

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"──「 **𝗵𝗲𝗹𝗽 𝗳𝗼𝗿я {str(help_arg).upper()}** 」──\n\n"
            for x in commands:
                this_command += f"  •  **𝗖𝗼𝗺𝗺𝗮𝗻𝗱:** `.{str(x)}`\n  •  **𝗙𝘂𝗻𝗰𝘁𝗶𝗼𝗻:** `{str(commands[x])}`\n\n"
            this_command += "@DETECTED_09"
            await edit_or_reply(
                message, this_command, parse_mode=enums.ParseMode.MARKDOWN
            )
        else:
            await edit_or_reply(
                message,
                f"`{help_arg}` **𝗻𝗼𝘁 𝗮 𝘃𝗮𝗹𝗶𝗱 𝗺𝗼𝗱𝘂𝗹𝗲 𝗻𝗮𝗺𝗲.**",
            )


@Client.on_message(filters.command(["plugins", "modules"], ".") & filters.me)
async def module_helper(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        help_arg = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        ac = PrettyTable()
        ac.header = False
        ac.title = "𝗧𝗵𝗲-𝗧𝗶𝗴𝗲𝗿𝗫"
        ac.align = "l"
        for x in split_list(sorted(CMD_HELP.keys()), 2):
            ac.add_row([x[0], x[1] if len(x) >= 2 else None])
        await edit_or_reply(
            message, f"```{str(ac)}```\n@The_Tiger_X ⚡ @DETECTED_09 "
        )
        await message.reply(
            f"**𝗧𝗵𝗲-𝗧𝗶𝗴𝗲𝗿𝗫**"
        )

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"──「 **𝗵𝗲𝗹𝗽 𝗳𝗼𝗿 {str(help_arg).upper()}** 」──\n\n"
            for x in commands:
                this_command += f"  •  **𝗖𝗼𝗺𝗺𝗮𝗻𝗱:** `.{str(x)}`\n  •  **𝗙𝘂𝗻𝗰𝘁𝗶𝗼𝗻𝘀:** `{str(commands[x])}`\n\n"
            this_command += " @DETECTED_09 "
            await edit_or_reply(
                message, this_command, parse_mode=enums.ParseMode.MARKDOWN
            )
        else:
            await edit_or_reply(
                message,
                f"`{help_arg}` **𝗡𝗼𝘁 𝗮 𝘃𝗮𝗹𝗶𝗱∂ 𝗺𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲.**",
            )


def add_command_help(module_name, commands):
    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict
