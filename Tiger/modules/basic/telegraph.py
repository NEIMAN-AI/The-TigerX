from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import Telegraph, exceptions, upload_file
import os



telegraph = Telegraph()
r = telegraph.create_account(short_name="telegram")
auth_url = r["auth_url"]



def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

@Client.on_message(filters.command(["tg", "telegraph", "tm", "tgt"], ".") & filters.me)
async def uptotelegraph(client: Client, message: Message):
    tex = await message.edit_text("`𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴. . . .`")
    if not message.reply_to_message:
        await tex.edit(
            "**𝗥𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮𝗻 𝗜𝗺𝗮𝗴𝗲 𝗼𝗿 𝘁𝗲𝘅𝘁.**"
        )
        return
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await tex.edit(f"**𝗘𝗥𝗥𝗢𝗥:** `{exc}`")
            os.remove(m_d)
            return
        U_done = (
            f"**𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 𝗼𝗻 ** [Telegraph](https://telegra.ph/{media_url[0]})"
        )
        await tex.edit(U_done)
        os.remove(m_d)
    elif message.reply_to_message.text:
        page_title = get_text(message) if get_text(message) else client.me.first_name
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            await tex.edit(f"**𝗘𝗥𝗥𝗢𝗥...:** `{exc}`")
            return
        wow_graph = f"**𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 𝗮𝘀..** [Telegraph](https://telegra.ph/{response['path']})"
        await tex.edit(wow_graph)

