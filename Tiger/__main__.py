import asyncio
import importlib
from pyrogram import Client, idle
from Tiger.helper import join
from Tiger.modules import ALL_MODULES
from Tiger import clients, app, ids

async def start_bot():
    await app.start()
    print("LOG: ғᴏᴜɴᴅᴇᴅ ʙᴏᴛ ᴛᴏᴋᴇɴ ʙᴏᴏᴛɪɴɢ..")
    for all_module in ALL_MODULES:
        importlib.import_module("Tiger.modules" + all_module)
        print(f"sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ {all_module} ⚡")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"sᴛᴀʀᴛᴇᴅ {ex.first_name} ⚡")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
