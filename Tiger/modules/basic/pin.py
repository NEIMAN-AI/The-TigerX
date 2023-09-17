import asyncio

from pyrogram import filters, Client
from pyrogram.methods.chats.get_chat_members import Filters as ChatMemberFilters
from pyrogram.types import Message


@Client.on_message(filters.command("pin", ".") & filters.me)
async def pin_message(_, message: Message):
    # First of all check if its a group or not
    if message.chat.type in ["group", "supergroup"]:
        # Here lies the sanity checks
        admins = await UserBot.get_chat_members(
            message.chat.id, filter=ChatMemberFilters.ADMINISTRATORS
        )
        admin_ids = [user.user.id for user in admins]
        me = await UserBot.get_me()

        # If you are an admin
        if me.id in admin_ids:
            # If you replied to a message so that we can pin it.
            if message.reply_to_message:
                disable_notification = True

                # Let me see if you want to notify everyone. People are gonna hate you for this...
                if len(message.command) >= 2 and message.command[1] in [
                    "alert",
                    "notify",
                    "loud",
                ]:
                    disable_notification = False

                # Pin the fucking message.
                await UserBot.pin_chat_message(
                    message.chat.id,
                    message.reply_to_message.message_id,
                    disable_notification=disable_notification,
                )
                await message.edit("𝗣𝗶𝗻𝗻𝗲𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗯𝗮𝗯𝗲...!")
            else:
                # You didn't reply to a message and we can't pin anything. ffs
                await message.edit(
                    "𝗥𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘀𝗼 𝘁𝗵𝗮𝘁 𝗜 𝗰𝗮𝗻 𝗽𝗶𝗻 𝘁𝗵𝗲 𝗴𝗼𝗱 𝗱𝗮𝗺𝗻𝗲𝗱 𝘁𝗵𝗶𝗻𝗴...."
                )
        else:
            # You have no business running this command.
            await message.edit("𝗜 𝗮𝗺 𝗻𝗼𝘁 𝗮𝗻 𝗮𝗱𝗺𝗶𝗻 𝗵𝗲𝗿𝗲 𝗹𝗺𝗮𝗼. 𝗪𝗵𝗮𝘁 𝗮𝗺 𝗜 𝗱𝗼𝗶𝗻𝗴?")
    else:
        # Are you fucking dumb this is not a group ffs.
        await message.edit("𝗧𝗵𝗶𝘀 𝗶𝘀 𝗻𝗼𝘁 𝗮 𝗽𝗹𝗮𝗰𝗲 𝘄𝗵𝗲𝗿𝗲 𝗜 𝗰𝗮𝗻 𝗽𝗶𝗻 𝘀𝗵𝗶𝘁.")

    # And of course delete your lame attempt at changing the group picture.
    # RIP you.
    # You're probably gonna get ridiculed by everyone in the group for your failed attempt.
    # RIP.
    await asyncio.sleep(3)
    await message.delete()
