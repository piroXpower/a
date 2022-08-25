import asyncio
import math
import os
import time
from datetime import datetime
import sys
import heroku3
import requests

heroku_api = "https://api.heroku.com"
Heroku = heroku3.from_key(HEROKU_API_KEY)

from hackingaibot import hn, BotClient, HEROKU_APP_NAME, HEROKU_API_KEY, SUDO_USERS, DEV_USERS

@BotClient.on(events.NewMessage(incoming=True, pattern=r"^/restart(?: |$)(.*)", forwards=False))
@BotClient.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hn, forwards=False))
async def dyno_usage(dyno):
    if dyno.fwd_from:
        return
    if int(dyno.sender_id) in DEV_USERS or int(dyno.sender_id) in SUDO_USERS:
        pass
    else:
        return
    lol = await dyno.reply("**Processing...**")
    await lol.edit("**Restarting bot...**\nPlease wait 1-2 minutes...\nTo check if bot is awake use /ping command.")
    args = [sys.executable, "-m", "hackingaibot"]
    os.execl(sys.executable, *args)
