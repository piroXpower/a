# Gladiators - Hacking-AiBot
# Copyright (C) 2022-Present Gladiators-Projects
# This was licensed under GNU General Public License v3.0 < https://github.com/Gladiators-Projects/Hacking-AiBot/blob/main/LICENSE >
#
# This file is a part of < https://github.com/Gladiators-Projects/Hacking-AiBot >


import logging
import os
import sys
from inspect import getfullargspec
from os import getenv
from decouple import config
import time
from datetime import datetime
from telethon import TelegramClient
from telethon.sessions import StringSession

REPO_NAME =  "Hacking-AiBot"
StartTime = time.time()

# logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

API_ID = config("API_ID", "14294016", cast=int)
API_HASH = config("API_HASH", "c103b212d630bf084ca1f150729d07c5")
OWNER_ID = config("OWNER_ID", "5582758633")
BOT_ID = config("BOT_ID", "5358198634", cast=int)
BOT_USERNAME = config("BOT_USERNAME", "TestSpamOkBot")
HEROKU_API_KEY = config("HEROKU_API_KEY", default=None)
HEROKU_APP_NAME  = config("HEROKU_APP_NAME", default=None)
Bot_Token = config("Bot_Token", "5358198634:AAHELIJ_iiT2BFNbZ3rHRQeLaBQ06uPl2KM")
HNDLR = config("HANDLER", "/")
SUDO_USERS = list(map(int, config("SUDO_USERS", "5582758633").split()))
DEV_USERS = list(map(int, config("DEV_USERS", "5582758633").split()))
hn = HNDLR #lay-z af

SUDO_USERS.append(OWNER_ID)
DEV_USERS.append(OWNER_ID)
SUDO_USERS = list(SUDO_USERS)
DEV_USERS = list(DEV_USERS)

#TELETHON BOT
print("[INFO]: STARTING TELETHON BOT CLIENT")
BotClient = TelegramClient('Bot', API_ID, API_HASH).start(bot_token=Bot_Token)
