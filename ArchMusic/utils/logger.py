

from config import LOG, LOG_GROUP_ID
import psutil
import time
from ArchMusic import app
from ArchMusic.utils.database import is_on_off
from ArchMusic.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)
from ArchMusic.utils.database import (get_global_tops,
                                       get_particulars, get_queries,
                                       get_served_chats,
                                       get_served_users, get_sudoers,
                                       get_top_chats, get_topp_users)



async def play_logs(message, streamtype):
    chat_id = message.chat.id
    sayı = await app.get_chat_members_count(chat_id)
    toplamgrup = len(await get_served_chats())
    aktifseslisayısı = len(await get_active_chats())
    aktifvideosayısı = len(await get_active_video_chats())
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    CPU = f"{cpu}%"
    RAM = f"{mem}%"
    DISK = f"{disk}%"


    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Gizli Grup"
        logger_text = f"""


**Grup:** {message.chat.title} [`{message.chat.id}`]
**Üye Sayısı: 👉{sayı}**
**Kullanıcı:** {message.from_user.mention}
**Kullanıcı Adı:** @{message.from_user.username}
**Kullanıcı ID:** `{message.from_user.id}`
**Grup Linki:** {chatusername}
**Sorgu:** {message.text}

**CPU:** {CPU}  ❄️  **RAM:** {RAM}  ❄️  **DISK:** {DISK}

**Toplam Grup Sayısı: 👉{toplamgrup}**

**Aktif Ses: {aktifseslisayısı}  ❄️  Aktif Video: {aktifvideosayısı}**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
                await app.set_chat_title(LOG_GROUP_ID, f"AKTİF SES - {aktifseslisayısı}")
            except:
                pass
        return
