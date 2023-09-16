import requests
from bs4 import BeautifulSoup
from googlesearch import search
from pyrogram import Client, filters
from pyrogram.types import Message

from Tiger.helper.basic import edit_or_reply

from Tiger.modules.help import *


def googlesearch(query):
    co = 1
    returnquery = {}
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        url = str(j)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        metas = soup.find_all("meta")
        site_title = None
        for title in soup.find_all("title"):
            site_title = title.get_text()
        metadeta = [
            meta.attrs["content"]
            for meta in metas
            if "name" in meta.attrs and meta.attrs["name"] == "description"
        ]
        returnquery[co] = {"title": site_title, "metadata": metadeta, "url": j}
        co = co + 1
    return returnquery


@Client.on_message(filters.command(["gs", "google"], ".") & filters.me)
async def gs(client: Client, message: Message):
    Man = await edit_or_reply(message, "`𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴.....`")
    msg_txt = message.text
    returnmsg = ""
    query = None
    if " " in msg_txt:
        query = msg_txt[msg_txt.index(" ") + 1 : len(msg_txt)]
    else:
        await Man.edit("𝗚𝗶𝘃𝗲 𝗮 𝗾𝘂𝗲𝗿𝘆 𝘁𝗼 𝘀𝗲𝗮𝗿𝗰𝗵 𝗯𝗮𝗯𝗲....")
        return
    results = googlesearch(query)
    for i in range(1, 10, 1):
        presentquery = results[i]
        presenttitle = presentquery["title"]
        presentmeta = presentquery["metadata"]
        presenturl = presentquery["url"]
        print(presentquery)
        print(presenttitle)
        print(presentmeta)
        print(presenturl)
        if not presentmeta:
            presentmeta = ""
        else:
            presentmeta = presentmeta[0]
        returnmsg = (
            returnmsg
            + f"[{str(presenttitle)}]({str(presenturl)})\n{str(presentmeta)}\n\n"
        )
    await Man.edit(returnmsg)


add_command_help(
    "google",
    [
        [
            "google",
            "𝗙𝗲𝗮𝘁𝗰𝗵 𝗗𝗲𝘁𝗮𝗶𝗹𝘀 𝗼𝗻 𝗚𝗼𝗼𝗴𝗹𝗲.",
        ],
    ],
)
