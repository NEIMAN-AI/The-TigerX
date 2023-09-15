import time
from datetime import datetime

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from Tiger import StartTime, app, SUDO_USER
from Tiger.helper.PyroHelpers import SpeedConvert
from Tiger.modules.bot.inline import get_readable_time

from Tiger.modules.help import add_command_help

class WWW:
    SpeedTest = (
        "Speedtest started at `{start}`\n\n"
        "Ping:\n{ping} ms\n\n"
        "Download:\n{download}\n\n"
        "Upload:\n{upload}\n\n"
        "ISP:\n__{isp}__"
    )

    NearestDC = "Country: `{}`\n" "Nearest Datacenter: `{}`\n" "This Datacenter: `{}`"

@Client.on_message(
    filters.command(["speedtest"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def speed_test(client: Client, message: Message):
    new_msg = await message.reply_text("`яυииιиg ѕρєєᴅ тєѕт . . .`⚡")
    try:
       await message.delete()
    except:
       pass
    spd = speedtest.Speedtest()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`вєѕт ѕєяνєя вαѕє∂ σи ριиg ⚡. . .`"
    )
    spd.get_best_server()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`∂σωиℓσα∂ ѕρєє∂ ⚡ . . .`")
    spd.download()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`υρℓσα∂ ѕρєє∂ ⚡ . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "` ρяєραяιиg fσямαттιиg ⚡. . .`"
    )
    results = spd.results.dict()

    await new_msg.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )



@Client.on_message(
    filters.command(["ping"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**⚡ᴘɪɴɢ ᴘᴏɴɢ⚡**")
    try:
       await message.delete()
    except:
       pass
    await xx.edit("**𝗧𝗵𝗲 𝗧𝗶𝗴𝗲𝗿𝗫**")
    await xx.edit("**ᴘᴏɴɢ.**")
    await xx.edit("**ᴘᴏɴɢ..**")
    await xx.edit("**ᴘᴏɴɢ...**")
    await xx.edit("**ᴘᴏɴɢ.....**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f" **𝗧𝗵𝗲-𝗧𝗶𝗴𝗲𝗿𝗫**\n "
        f"🏓 𝗣𝗢𝗡𝗚 🏓\n"
        f"**»** - `%sms`\n"
        f"**» -** `{uptime}` \n"
        f"**» -** {client.me.mention}" % (duration)
    )


add_command_help(
    "ping",
    [
        ["ping", "🏓ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ⚡."],
    ],
)
