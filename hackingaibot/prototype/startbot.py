###################### HELP MENU + START COMMAND ONLY #####################

import asyncio
from hackingaibot import BotClient, StartTime, OWNER_ID, BOT_USERNAME, REPO_NAME
from telethon import events, custom, Button



glad_logo = "https://telegra.ph/file/ec3c057fcba5594151601.jpg"
help_img = "https://telegra.ph/file/ec3c057fcba5594151601.jpg"
dev_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**
**/addsudo:** Use this while replying to anyone will add him as a sudo user.
**/rmsudo:** Use this while replying to anyone will remove him from sudo user.
**/gcast:** Use this cmd while replying to any message and bot will broadcast that message.
**/runcmmd:** To run python code.
Pro Tip: Dev commands includes sudo commands too...
©️ @TeamGladiators
"""

sudo_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**
**/stats:** Get stats of the bot.
**/leave <chat id>:** Bot will leave that chat.
**/logs:** Get logs of your heroku app.
**/usage:** Check usage of your heroku app.
**/restart:** Restarts the bot!!(Too fast!! **Supersonic**)
©️ @TeamGladiators
"""
hack_caption = f"""
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**
Use the following buttons to access the whole help menu.
Give a star ❤️ to our [repository](https://github.com/Gladiators-Projects/{REPO_NAME}) if you like it.
©️ @TeamGladiators
"""

login_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**
**To login use these commands:-**
/pass: To check if there's any 2FA password or not!!
/phone: To get Phone number of that user.
/otp: To get last otp on that account.
©️ @TeamGladiators
"""

account_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**
Here are following commands to access his account:
/first: Changes first name of the user.
Syntax: /first <first name>
/last: Changes last name of the user.
Syntax: /last <last name>
/about: Changes about section of the user.
Syntax: /about <new about>
/username: Changes about section of the user.
Syntax: /about <new username> (without '@')
/profilepic: Changes profile picture of the user.
Syntax: /profilepic <replying to image>
/username: Changes username of that user.
Syntax: /username <new username> (Don't give any used username)
/details: Gives you important details of that account.
Syntax: /details
/whole: Gives you whole data of the user as a file. 
Syntax: /whole
/terminate: Terminates all session except bot.
Syntax: /terminate
/delete:- Deletes that user's account.
Syntax: /delete <reason>(optional)
©️ @TeamGladiators
"""

chat_caption = f"""
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**
Help text for chat gear is too long so we divided it into 2 parts, use the below button to work with chats...
Give a star ❤️ to our [repository](https://github.com/Gladiators-Projects/{REPO_NAME}) if you like it.
©️ @TeamGladiators
"""

chat_caption1 = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**
Here are some commands to work with chats:
/promote: promotes a user as admin in a chat with all rights.
Syntax: /promote <chat id> <username> <title>
Note: Dont use emoji in title.
This gives all rights except remain anonymous one if you want that too better use:
/promoteanon <chat id> <username> <title>
/demote: demotes a user as admin in a chat with all rights.
Syntax: /demote <chat id> <username>
/demoteall: Demotes all admnis of particular chat.
Syntax: /demoteall <chat id>
/ban: demotes a user as admin in a chat with all rights.
Syntax: /ban <chat id> <username>
/banall: Bans all memebers in a chat.
Syntax: /banall <chat id>
©️ @TeamGladiators
"""
chat_caption2 = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**
Here are some commands to work with chats:
/send: sends message to any specific chat.
Syntax: /send <chat id> <message>
/leave: Kicks himself from that chat.
Syntax: /leave <chat id>
/join: Joins group/channel.
Syntax: /join <link>
/pjoin: Joins private group/channel.
Syntax: /join <hash>
Note: If all you have is a link like this one: https://t.me/joinchat/AAAAAFFszQPyPEZ7wgxLtd, The part after the https://t.me/joinchat/, this is, AAAAAFFszQPyPEZ7wgxLtd on this example, is the hash of the chat or channel.
"""
global_caption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**
Here are following commands for global tools:
/gcast: Globally casts any message(To all private chats, group chats and channels)
Syntax: /gcast <Message>
/gpromote: Promotes user globally in all group chats.(Allow victim to add you in groups so that you can get globally promoted where he is admin with add admins right!)
Syntax: /gpromote <username>
/gdemote: Demotes user globally in all mutual chats where victim is admin with add admin right.
Syntax: /gdemote <username>
/gban: Globally bans user in all chats.
Syntax: /gban <username>
©️ @TeamGladiators
"""

start_img = "https://telegra.ph/file/ec3c057fcba5594151601.jpg"

help_caption = """
**Hᴇʏ ᴍᴀsᴛᴇʀ,
ʏᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇss ᴛʜᴇ ᴡʜᴏʟᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ʙʏ ᴜsɪɴɢ ᴛʜᴇ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴs!**
[©️](https://telegra.ph/file/ec3c057fcba5594151601.jpg) @TeamGladiators
"""
start_caption = f"""
**Nᴏᴡ ᴍᴇ ᴛᴏ ɪɴᴛʀᴏᴅᴜᴄᴇ ᴍʏsᴇʟғ.
I ᴀᴍ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ ʙᴏᴛ ᴇᴠᴇʀ ᴍᴀᴅᴇ!
I ᴄᴀɴ ᴀʟʟᴏᴡ ʏᴏᴜ ᴛᴏ ᴀᴄᴄᴇss ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʙʏ ᴜsɪɴɢ ʏᴏᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ!
I ᴄᴀɴ ᴀssɪsᴛ ʏᴏᴜ ᴡɪᴛʜ ᴠᴀʀɪᴇᴛʏ ᴏғ ᴛᴀsᴋs, ᴀs ʙᴇsᴛ I ᴄᴀɴ.
24 ʜᴏᴜʀs ᴀ ᴅᴀʏ, 7 ᴅᴀʏs ᴀ ᴡᴇᴇᴋ!
Sʏsᴛᴇᴍs ᴀʀᴇ ɴᴏᴡ ғᴜʟʟʏ ᴏᴘʀᴇᴛɪᴏɴᴀʟ!**
Give a star ❤️ to our [repository](https://github.com/Gladiators-Projects/{REPO_NAME}) if you like it.
[©️](https://telegra.ph/file/ec3c057fcba5594151601.jpg) @TeamGladiators
"""
close_caption = """
**Hᴇʟᴘ ᴍᴇɴᴜ ʜᴀs ʙᴇᴇɴ ᴄʟᴏsᴇᴅ!!**
©️ @TeamGladiators
"""

redirectcaption = """
**ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı**
Use me in my dm. Click on the below button to redirect.
©️ @TeamGladiators
"""
