from config import Messages
from time import time, sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired, UserAdminInvalid


@Client.on_message(filters.incoming & ~filters.private & filters.command(['inkick']))
def inkick(client, message):
  user = client.get_chat_member(message.chat.id, message.from_user.id)
  if user.status == "creator":
    if len(message.command) > 1:
      input_str = message.command
      sent_message = message.reply_text(Messages.START_KICK)
      count = 0
      for member in client.iter_chat_members(message.chat.id):
        if member.user.status in input_str and not member.status in ('administrator', 'creator'):
          try:
            client.kick_chat_member(message.chat.id, member.user.id, int(time() + 45))
            count += 1
            sleep(1)
          except (ChatAdminRequired, UserAdminInvalid):
            sent_message.edit(Messages.ADMIN_REQUIRED)
            client.leave_chat(message.chat.id)
            break
          except FloodWait as e:
            sleep(e.x)
      try:
        sent_message.edit(Messages.KICKED.format(count))
      except ChatWriteForbidden:
        pass
    else:
      message.reply_text(Messages.INPUT_REQUIRED)
  else:
    sent_message = message.reply_text(Messages.CREATOR_REQUIRED)
    sleep(5)
    sent_message.delete()

@Client.on_message(filters.incoming & ~filters.private & filters.command(['dkick']))
def dkick(client, message):
  user = client.get_chat_member(message.chat.id, message.from_user.id)
  if user.status == "creator":
    sent_message = message.reply_text(Messages.START_KICK)
    count = 0
    for member in client.iter_chat_members(message.chat.id):
      if member.user.is_deleted and not member.status in ('administrator', 'creator'):
        try:
          client.kick_chat_member(message.chat.id, member.user.id, int(time() + 45))
          count += 1
          sleep(1)
        except (ChatAdminRequired, UserAdminInvalid):
          sent_message.edit(Messages.ADMIN_REQUIRED)
          client.leave_chat(message.chat.id)
          break
        except FloodWait as e:
          sleep(e.x)
    try:
      sent_message.edit(Messages.DKICK.format(count))
    except ChatWriteForbidden:
      pass
  else:
    sent_message = message.reply_text(Messages.CREATOR_REQUIRED)
    sleep(5)
    sent_message.delete()
