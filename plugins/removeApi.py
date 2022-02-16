#!/usr/bin/env python3


### Importing
from botModule.importCommon import *


### Start & Help Handler
@Client.on_message(filters.private & filters.command("revoke"))
async def removeApiHandler(bot:Update, msg:Message):
    if await search_user_in_community(bot, msg):
        userid = msg.chat.id
        if apiExist(userid):
            removeApiKey(userid)
            await msg.reply_text(
                "<b>Yᴏᴜʀ Aᴘɪ Kᴇʏ Is Rᴇᴍᴏᴠᴇᴅ Sᴜᴄᴄᴇssꜰᴜʟʟʏ 😭</b>",
                parse_mode = "html"
            )
        else:
            await msg.reply_text(
                "<b>I Aᴍ Uɴᴀʙʟᴇ Tᴏ Fɪɴᴅ Yᴏᴜʀ Aᴘɪ Kᴇʏ Iɴ Dᴀᴛᴀʙᴀsᴇ.\nMᴀᴋᴇ Sᴜʀᴇ Iᴛ Wᴀs Aᴅᴅᴇᴅ Bᴇꜰᴏʀᴇ.</b>",
                parse_mode = "html"
            )
    return

