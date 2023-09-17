from Tiger.modules.help import *
import os
from pyrogram import filters, Client
from pyrogram.types import Message
from py_trans import Async_PyTranslator
from Tiger.helper.utility import get_arg



@Client.on_message(filters.command(["tr", "translate"], ["."]) & filters.me)
async def pytrans_tr(_, message: Message):
  tr_msg = await message.edit("`𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴....`")
  r_msg = message.reply_to_message
  args = get_arg(message)
  if r_msg:
    if r_msg.text:
      to_tr = r_msg.text
    else:
      return await tr_msg.edit("`𝗥𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘁𝗵𝗮𝘁 𝗰𝗼𝗻𝘁𝗮𝗶𝗻𝘀 𝘁𝗲𝘅𝘁 𝗯𝗮𝗯𝗲..!`")
    # Checks if dest lang is defined by the user
    if not args:
      return await tr_msg.edit(f"`𝗣𝗹𝗲𝗮𝘀𝗲 𝗱𝗲𝗳𝗶𝗻𝗲 𝗮 𝗱𝗲𝘀𝘁𝗶𝗻𝗮𝘁𝗶𝗼𝗻 𝗹𝗮𝗻𝗴𝘂𝗮𝗴𝗲!` \n\n**Ex:** `{Config.CMD_PREFIX}ptr 𝘀𝗶 𝗛𝗲𝘆, 𝗜𝗺 𝘂𝘀𝗶𝗻𝗴 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗯𝗮𝗯𝗲...!`")
    # Setting translation if provided
    else:
      sp_args = args.split(" ")
      if len(sp_args) == 2:
        dest_lang = sp_args[0]
        tr_engine = sp_args[1]
      else:
        dest_lang = sp_args[0]
        tr_engine = "google"
  elif args:
    # Splitting provided arguments in to a list
    a_conts = args.split(None, 2)
    # Checks if translation engine is defined by the user
    if len(a_conts) == 3:
      dest_lang = a_conts[0]
      tr_engine = a_conts[1]
      to_tr = a_conts[2]
    else:
      dest_lang = a_conts[0]
      to_tr = a_conts[1]
      tr_engine = "google"
  # Translate the text
  py_trans = Async_PyTranslator(provider=tr_engine)
  translation = await py_trans.translate(to_tr, dest_lang)
  # Parse the translation message
  if translation["status"] == "success":
    tred_txt = f"""
**Translation Engine**: `{translation["engine"]}`
**Translated to:** `{translation["dest_lang"]}`
**Translation:**
`{translation["translation"]}`
"""
    if len(tred_txt) > 4096:
      await tr_msg.edit("`!! 𝗧𝗿𝗮𝗻𝘀𝗹𝗮𝘁𝗲𝗱 𝗧𝗲𝘅𝘁 𝗦𝗼 𝗟𝗼𝗻𝗴 𝗧𝗵𝗼!, 𝗚𝗶𝘃𝗲 𝗺𝗲 𝗮 𝗺𝗶𝗻𝘂𝘁𝗲, 𝗜𝗺 𝘀𝗲𝗻𝗱𝗶𝗻𝗴 𝗶𝘁 𝗮𝘀 𝗮 𝗳𝗶𝗹𝗲 𝗯𝗮𝗯𝗲...!`")
      tr_txt_file = open("translated.txt", "w+")
      tr_txt_file.write(tred_txt)
      tr_txt_file.close()
      await tr_msg.reply_document("ptranslated_NEXAUB.txt")
      os.remove("ptranslated.txt")
      await tr_msg.delete()
    else:
      await tr_msg.edit(tred_txt)

