import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Tiger"])

async def join(client):
    try:
        await client.join_chat("DETECTED_09")
    except BaseException:
        pass
