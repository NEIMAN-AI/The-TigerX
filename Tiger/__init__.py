from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION
from datetime import datetime
import time
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)
aiosession = ClientSession()

if API_ID:
   API_ID = API_ID
else:
   print("𝗪𝗔𝗥𝗡𝗜𝗡𝗚: ᴀᴘɪ ɪᴅ ɴᴏᴛ ғᴏᴜɴᴅ ⚡")
   API_ID = "6435225"

if API_HASH:
   API_HASH = API_HASH
else:
   print("𝗪𝗔𝗥𝗡𝗜𝗡𝗚: ᴀᴘɪ ʜᴀsʜ ɴᴏᴛ ғᴏᴜɴᴅ⚡")   
   API_HASH = "4e984ea35f854762dcde906dce426c2d"

if not BOT_TOKEN:
   print("𝗪𝗔𝗥𝗡𝗜𝗡𝗚: ʙᴏᴛ ᴛᴏᴋᴇɴ ɴᴏᴛ ғᴏᴜɴᴅ ⚡")   

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Tiger/modules/bot"),
    in_memory=True,
)

if STRING_SESSION:
   print("Client: ғᴏᴜɴᴅ.. sᴛᴀʀᴛɪɴɢ...")
   client = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION, plugins=dict(root="Tiger/modules"))
   clients.append(client)
