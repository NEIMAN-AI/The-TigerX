import os

from pyrogram import *
from pyrogram.types import *


from Tiger.helper.basic import edit_or_reply, get_text, get_user

from Tiger.modules.help import *

OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "𝗧𝗵𝗲-𝗧𝗶𝗴𝗲𝗿𝗫 © @The_Tiger_X ")


@Client.on_message(filters.command("clone", ".") & filters.me)
async def clone(client: Client, message: Message):
    text = get_text(message)
    op = await message.edit_text("`𝗖𝗹𝗼𝗻𝗶𝗻𝗴.....`")
    userk = get_user(message, text)[0]
    user_ = await client.get_users(userk)
    if not user_:
        await op.edit("`𝗪𝗵𝗼𝗺 𝗶 𝘀𝗵𝗼𝘂𝗹𝗱 𝗰𝗹𝗼𝗻𝗲..:(`")
        return

    get_bio = await client.get_chat(user_.id)
    f_name = user_.first_name
    c_bio = get_bio.bio
    pic = user_.photo.big_file_id
    poto = await client.download_media(pic)

    await client.set_profile_photo(photo=poto)
    await client.update_profile(
        first_name=f_name,
        bio=c_bio,
    )
    await message.edit(f"**𝗙𝗿𝗼𝗺 𝗻𝗼𝘄 𝗜 𝗺** __{f_name}__")


@Client.on_message(filters.command("revert", ".") & filters.me)
async def revert(client: Client, message: Message):
    await message.edit("`𝗥𝗲𝘃𝗲𝗿𝘁𝗶𝗻𝗴...`")
    r_bio = BIO

    # Get ur Name back
    await client.update_profile(
        first_name=OWNER,
        bio=r_bio,
    )
    # Delte first photo to get ur identify
    photos = [p async for p in client.get_chat_photos("me")]
    await client.delete_profile_photos(photos[0].file_id)
    await message.edit("`𝗜 𝗮𝗺 𝗯𝗮𝗰𝗸!`")


add_command_help(
    "clone",
    [
        ["clone", "𝗧𝗼 𝗖𝗹𝗼𝗻𝗲 𝘀𝗼𝗺𝗲𝗼𝗻𝗲 𝗣𝗿𝗼𝗳𝗶𝗹𝗲...."],
        ["revert", "𝗧𝗼 𝗚𝗲𝘁 𝗬𝗼𝘂𝗿 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗕𝗮𝗰𝗸..."],
    ],
)
