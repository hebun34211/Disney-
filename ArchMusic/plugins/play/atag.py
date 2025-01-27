import os, logging, asyncio
from ArchMusic import app
from ArchMusic.utils.database import set_cmode
from ArchMusic.utils.decorators.admins import AdminActual
from telethon import events, Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
 

import time, random 

# Silmeyiniz. 
anlik_calisan = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}
# ---------------------------- Komutlar ---------------------------
@app.on_message(filters.command("cancel") & filters.group)
async def cancel_tag(client, message: Message):
    admins = []
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if message.from_user.id not in admins:
        await message.reply("**Bu komutu kullanmak için yönetici olmalısınız! 😉**")
        return
        
    if message.chat.id in rose_tagger:
        del rose_tagger[message.chat.id]
        active_tags.pop(message.chat.id, None)
        await message.reply(f"⛔ **Etiketleme işlemi durduruldu!**\n\n❤️‍🔥 **İşlem'i durduran: {message.from_user.mention}**")
    else:
        await message.reply("ℹ️ **Etiketleme işlemi şu anda aktif değil.**")

# -------------------Tagger-------------------------------
@ArchMusic.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan 
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**▸ʜᴀᴛᴀ ʙᴜ ʙɪʀ ɢʀᴜᴘ ᴋᴏᴍᴜᴛᴜᴅᴜʀ**")
  
  admins = []
  async for admin in Maho.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**▸sᴀɴɪʀɪᴍ ɢʀᴜᴘᴛᴀ ʏᴏɴᴇᴛɪᴄɪ ᴅᴇɪʟsɪɴɪᴢ**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("🇭 🇦 🇹 🇦")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**▸ʜᴇʏ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇᴍ ɪᴄɪɴ sᴇʙᴇᴘ ᴠᴇʀᴍᴇʟɪsɪɴ ʙᴀɴᴀ**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**꙳ᴇᴛɪᴋᴇᴛ ɪsʟᴇᴍɪ ʙᴀsʟᴀᴅɪ꙳**")
        
    async for usr in ArchMusic.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}),"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 6:
        await Maho.send_message(event.chat_id, f"📢 ~ **{msg}**\n\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**▸ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ\n\n▸ᴇᴛɪᴋᴇᴛʟᴇɴᴇɴ ᴋᴜʟʟᴀɴɪᴄɪ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")
           await sleep(10)
           await a.delete()

  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in Maho.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}),"
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 6:
        await Maho.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:
           a = await event.respond(f"**▸ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ\n\n▸ᴇᴛɪᴋᴇᴛʟᴇɴᴇɴ ᴋᴜʟʟᴀɴɪᴄɪ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}**")
           await sleep(10)
           await a.delete()
