# Aghori - UserBot
# Copyright (C) 2020 TeamAghori


from telethon.errors import ChatSendInlineForbiddenError
from telethon.errors.rpcerrorlist import BotMethodInvalidError as bmi

from . import *

REPOMSG = (
    "• **AGHORI USERBOT** •\n\n",
    "• Repo - [Click Here](https://github.com/SHIVGULSHAN/AGHORIRAAVAN_USERBOT)\n",
    "• Addons - [Click Here](https://github.com/SHIVGULSHAN/AGHORIRAAVAN_USERBOT)\n",
    "• Support - @AGHORI_USERBOT",
)


@ultroid_cmd(pattern="repo$")
async def repify(e):
    try:
        q = await ultroid_bot.inline_query(asst.me.username, "repo")
        await q[0].click(e.chat_id)
        if e.sender_id == ultroid_bot.uid:
            await e.delete()
    except ChatSendInlineForbiddenError or bmi:
        await eor(e, REPOMSG)
