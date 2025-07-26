from config import LOG, LOG_GROUP_ID
import psutil
from ArchMusic import app
from ArchMusic.utils.database import is_on_off
from ArchMusic.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats
)
from ArchMusic.utils.database import get_served_chats


async def play_logs(message, streamtype):
    chat_id = message.chat.id
    user = message.from_user

    # Sistem Bilgileri
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    # Sohbet Bilgileri
    member_count = await app.get_chat_members_count(chat_id)
    total_groups = len(await get_served_chats())
    active_voice = len(await get_active_chats())
    active_video = len(await get_active_video_chats())

    # Kullanıcı adı kontrolü
    chat_username = f"@{message.chat.username}" if message.chat.username else "🔒 Gizli Grup"

    # Log kontrolü
    if await is_on_off(LOG):
        logger_text = f"""
<b>📢 Yeni Müzik Oynatıldı</b>

<b>📌 Grup:</b> {message.chat.title} [`{chat_id}`]
<b>🔗 Grup Linki:</b> {chat_username}
<b>👥 Üye Sayısı:</b> <code>{member_count}</code>

<b>👤 Kullanıcı:</b> {user.mention}
<b>✨ Kullanıcı Adı:</b> @{user.username}
<b>🆔 Kullanıcı ID:</b> <code>{user.id}</code>

<b>🎶 Sorgu:</b> <code>{message.text}</code>

<b>📊 Sistem Durumu:</b>
  ├─ CPU Kullanımı: <b>{cpu}%</b> ♨️
  ├─ RAM Kullanımı: <b>{ram}%</b> 📂
  └─ Disk Kullanımı: <b>{disk}%</b> 💾

<b>🗂 Genel Durum:</b>
  ├─ Toplam Gruplar: <b>{total_groups}</b>
  ├─ Aktif Sesli Sohbet: <b>{active_voice}</b> 🎙️
  └─ Aktif Video Sohbet: <b>{active_video}</b> 🎥
"""

        if chat_id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    logger_text,
                    disable_web_page_preview=True,
                    parse_mode="html"
                )
                await app.set_chat_title(LOG_GROUP_ID, f"🔊 Aktif Ses - {active_voice}")
            except Exception:
                pass
