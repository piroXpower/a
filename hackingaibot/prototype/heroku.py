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


@BotClient.on(events.NewMessage(incoming=True, pattern=r"^/(log|logs)(?: |$)(.*)", forwards=False))
@BotClient.on(events.NewMessage(incoming=True, pattern=r"\%s(log|logs)(?: |$)(.*)" % hn, forwards=False))
async def _(logg):
    if logg.fwd_from:
        return
    if int(logg.sender_id) in DEV_USERS:
        pass
    else:
        return
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        herokuapp = Heroku.app(HEROKU_APP_NAME)
    except:
        return await logg.reply(
            "Check if your Heroku API Key, Your App name are configured correctly in the heroku"
        )
    v = await logg.reply("Getting Logs....")
    with open("logs.txt", "w") as logstxt:
        logstxt.write(herokuapp.get_log())
    await v.edit("Got the logs wait a sec")
    await logg.client.send_file(
        logg.chat_id,
        "logs.txt",
        reply_to=logg.id,
        caption="@Gladiators_Projects Logs.",
    )

    await asyncio.sleep(5)
    await v.delete()
    return os.remove("logs.txt")
