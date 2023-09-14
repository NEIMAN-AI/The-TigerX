import asyncio
from time import time

from pyrogram.types import Message

from pyrogram import Client 
from Tiger.helper.interval import IntervalHelper


async def CheckAdmin(message: Message):
    """ᴄʜᴇᴄᴋ ɪғ ᴡᴇ ᴀʀᴇ ᴀɴ ᴀᴅᴍɪɴ."""
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await Client.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__ɪᴍ ɴᴏᴛ ᴀᴅᴍɪɴ!__👎🏻")
        await asyncio.sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin:
            return True
        elif SELF.can_restrict_members:
            return True
        else:
            await message.edit("__ɴᴏ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴍᴇᴍʙᴇʀs__⚠️")
            await asyncio.sleep(2)
            await message.delete()


async def CheckReplyAdmin(message: Message):
    """ᴄʜᴇᴄᴋ ɪғ ᴛʜᴇ ᴍᴇssᴀɢᴇ ɪs a ʀᴇᴘʟʏ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴜsᴇʀ."""
    if not message.reply_to_message:
        await message.edit("ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ɴᴇᴇᴅs ᴛᴏ ʙᴇ ᴀ ʀᴇᴘʟʏ✅")
        await asyncio.sleep(2)
        await message.delete()
    elif message.reply_to_message.from_user.is_self:
        await message.edit(f"I can't {message.command[0]} myself⚠️.")
        await asyncio.sleep(2)
        await message.delete()
    else:
        return True

    return False


async def Timer(message: Message):
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time()).split(".")[0] + secs.to_secs()[0])
    else:
        return 0


async def TimerString(message: Message):
    secs = IntervalHelper(message.command[1])
    return f"{secs.to_secs()[1]} {secs.to_secs()[2]}"


async def RestrictFailed(message: Message):
    await message.edit(f"ɪ ᴄᴀɴᴛ {message.command} ᴛʜɪs ᴜsᴇʀ.")
    await asyncio.sleep(2)
    await message.delete()
