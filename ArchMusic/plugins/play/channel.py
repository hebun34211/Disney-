#
# Copyright (C) 2021-2023 by ArchBots@Github, < https://github.com/ArchBots >.
#
# This file is part of < https://github.com/ArchBots/ArchMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/ArchBots/ArchMusic/blob/master/LICENSE >
#
# All rights reserved.
#

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus, ChatType
from pyrogram.types import Message
import random
import asyncio
from config import BANNED_USERS
from strings import get_command
from ArchMusic import app
from ArchMusic.utils.database import set_cmode
from ArchMusic.utils.decorators.admins import AdminActual

### Multi-Lang Commands
CHANNELPLAY_COMMAND = get_command("CHANNELPLAY_COMMAND")


@app.on_message(
    filters.command(CHANNELPLAY_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminActual
async def playmode_(client, message: Message, _):
    if len(message.command) < 2:
        return await message.reply_text(
            _["cplay_1"].format(
                message.chat.title, CHANNELPLAY_COMMAND[0]
            )
        )
    query = message.text.split(None, 2)[1].lower().strip()
    if (str(query)).lower() == "disable":
        await set_cmode(message.chat.id, None)
        return await message.reply_text("Channel Play Disabled")
    elif str(query) == "linked":
        chat = await app.get_chat(message.chat.id)
        if chat.linked_chat:
            chat_id = chat.linked_chat.id
            await set_cmode(message.chat.id, chat_id)
            return await message.reply_text(
                _["cplay_3"].format(
                    chat.linked_chat.title, chat.linked_chat.id
                )
            )
        else:
            return await message.reply_text(_["cplay_2"])
    else:
        try:
            chat = await app.get_chat(query)
        except:
            return await message.reply_text(_["cplay_4"])
        if chat.type != ChatType.CHANNEL:
            return await message.reply_text(_["cplay_5"])
        try:
            admins = app.get_chat_members(
                chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            )
        except:
            return await message.reply_text(_["cplay_4"])
        async for users in admins:
            if users.status == ChatMemberStatus.OWNER:
                creatorusername = users.user.username
                creatorid = users.user.id
        if creatorid != message.from_user.id:
            return await message.reply_text(
                _["cplay_6"].format(chat.title, creatorusername)
            )
        await set_cmode(message.chat.id, chat.id)
        return await message.reply_text(
            _["cplay_3"].format(chat.title, chat.id)
        )

rose_tagger = {}
active_tags = {}


@app.on_message(filters.command("ktag") & filters.group)
async def ktag(client, message):
        
    if message.chat.type == 'private':
        await message.reply("❗ **Bu komutu sadece gruplarda kullanabilirsiniz!**")
        return

    admins = []
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        admins.append(member.user.id)

    if message.from_user.id not in admins:
        await message.reply("❗ **Bu komutu kullanmak için yönetici olmalısınız!**")
        return

    if message.chat.id in active_tags:
        await message.reply("⚠️ **Şu anda zaten bir etiketleme işlemi devam ediyor.**")
        return

    args = message.command
    if len(args) > 1:
        msg_content = " ".join(args[1:])
    elif message.reply_to_message:
        msg_content = message.reply_to_message.text
        if msg_content is None:
            await message.reply("❗** Eski mesajı göremiyorum!**")
            return
    else:
        msg_content = ""

    total_members = 0
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if not user.is_bot and not user.is_deleted:
            total_members += 1

    num = 3
    estimated_time = (total_members // num) * 5

    start_msg = await message.reply(f"""
🌟 **Etiketleme işlemi başlıyor.**
👥 **Toplam Etiketlenecek Üye Sayısı: {total_members}**
⏳ **Tahmini Süre: {estimated_time // 60} dakika**
""")

    rose_tagger[message.chat.id] = start_msg.id
    active_tags[message.chat.id] = True
    nums = 3
    usrnum = 0
    skipped_bots = 0
    skipped_deleted = 0
    total_tagged = 0
    usrtxt = ""
    
    async for member in client.get_chat_members(message.chat.id):
        user = member.user
        if user.is_bot:
            skipped_bots += 1
            continue
        if user.is_deleted:
            skipped_deleted += 1
            continue
        usrnum += 1
        total_tagged += 1
        usrtxt += f"• [{user.first_name}](tg://user?id={user.id})\n"
        if message.chat.id not in rose_tagger or rose_tagger[message.chat.id] != start_msg.id:
            return
        if usrnum == nums:
            await client.send_message(message.chat.id, f"📢\n{usrtxt}")
            usrnum = 0
            usrtxt = ""
            await asyncio.sleep(5)

    await client.send_message(message.chat.id, f"""
✅ **Etiketleme işlemi tamamlandı.**
👥 **Etiketlenen üye: {total_tagged}**
🤖 **Atlanılan Bot Sayısı: {skipped_bots}**
💣 **Atlanılan Silinen Hesap Sayısı: {skipped_deleted}**
""")
    active_tags.pop(message.chat.id, None)


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



