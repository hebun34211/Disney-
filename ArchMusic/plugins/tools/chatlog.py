from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from config import LOGGER_ID
from ArchMusic import app

PHOTOS = "https://files.catbox.moe/j1d9dn.jpg"


@app.on_message(filters.new_chat_members)
async def join_watcher(_, message: Message):
    chat = message.chat
    try:
        invite_link = await app.export_chat_invite_link(chat.id)
    except:
        invite_link = "Davet bağlantısı mevcut değil."

    for member in message.new_chat_members:
        if member.id == (await app.get_me()).id:
            member_count = await app.get_chat_members_count(chat.id)
            caption = (
                f"📝 **yeni bir gruba müzik botu eklendi**\n\n"
                f"❅─────✧❅✦❅✧─────❅\n\n"
                f"📌 **sohbet adı:** `{chat.title}`\n"
                f"🍂 **grup ıd:** `{chat.id}`\n"
                f"🔐 **grup ismi:** @{chat.username if chat.username else 'Private'}\n"
                f"🛰 **grup ʟɪɴᴋ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ]({invite_link})\n"
                f"📈 **ɢʀᴏᴜᴘ sayisi:** `{member_count}`\n"
                f"🤔 **tarafından eklendi:** {message.from_user.mention}"
            )

            await app.send_photo(
                chat_id=LOGGER_ID,
                photo=PHOTOS,
                caption=caption,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("gizli ɢʀuᴘ 👀", url=invite_link if isinstance(invite_link, str) else "https://t.me/")]]
                ),
            )


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    me = await app.get_me()
    if message.left_chat_member.id != me.id:
        return

    remover = message.from_user.mention if message.from_user else "**ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ**"
    chat = message.chat

    text = (
        f"✫ **<u>#ʟᴇғᴛ_ɢʀᴏᴜᴘ</u>** ✫\n\n"
        f"📌 **grup ismi:** `{chat.title}`\n"
        f"🆔 **grup id:** `{chat.id}`\n"
        f"👤 **talep eden:** {remover}\n"
        f"🤖 **ʙᴏᴛ:** @{me.username}"
    )

    await app.send_message(LOGGER_ID, text)
