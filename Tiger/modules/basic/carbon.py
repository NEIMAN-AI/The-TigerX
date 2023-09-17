import asyncio
from io import BytesIO

from pyrogram import Client, filters
from pyrogram.types import Message

from Tiger import aiosession

from Tiger.helper.PyroHelpers import ReplyCheck



async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@Client.on_message(filters.command("carbon", ".") & filters.me)
async def carbon_func(client: Client, message: Message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    ex = await message.edit_text("`𝗣𝗿𝗲𝗽𝗮𝗿𝗶𝗻𝗴 𝗖𝗮𝗿𝗯𝗼𝗻.. . . .`")
    carbon = await make_carbon(text)
    await ex.edit("`𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴.. . . .`")
    await asyncio.gather(
        ex.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"**Carbonised by** {client.me.mention}",
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    carbon.close()


