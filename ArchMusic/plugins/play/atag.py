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


app.on_message(filters.command(["slap", "sille"]) & filters.group)
async def slap(client, message):
    if is_user_blocked(message.from_user.id):
        await message.reply("**Üzgünüm, bu komutu kullanma yetkiniz engellendi.** 🚫")
        return
        
    chat = message.chat
    if not message.reply_to_message:
        await message.reply_text("🚫 **Bir kullanıcıya cevap verin!**")
        return
    if message.reply_to_message.from_user.id == OWNER_ID:
        await message.reply_text(f"{random.choice(dontslapown)}")
        return
    if message.reply_to_message.from_user.id == BOT_ID:
        await message.reply_text(f"{random.choice(dontslapme)}")
        return
    

    atan = message.from_user
    yiyen = message.reply_to_message.from_user

    atan_mesaj = f"[{atan.first_name}](tg://user?id={atan.id})"
    yiyen_mesaj = f"[{yiyen.first_name}](tg://user?id={yiyen.id})"

    goktug = random.choice(slapmessage)
    await message.reply_text(
        goktug.format(atan_mesaj, yiyen_mesaj),
    )

    await bot.send_message(
        LOG_CHANNEL,
        f"""
👤 Kullanan : [{atan.first_name}](tg://user?id={atan.id})
💥 Kullanıcı Id : {atan.id}
🪐 Kullanılan Grup : {chat.title}
💡 Grup ID : {chat.id}
◀️ Grup Link : @{chat.username}
📚 Kullanılan Modül : {message.text}
"""
    )
