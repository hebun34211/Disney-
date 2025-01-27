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

chatMode = []

chat_mode_users = {}

        await asyncio.sleep(0.06)          

    elif kontrol(["aç","ac","açç"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(aç)
        await asyncio.sleep(0.06)  

    elif kontrol(["barışalım","batısalım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(barışalım)
        await asyncio.sleep(0.06)   

    elif kontrol(["şimdi"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(şimdi)
        await asyncio.sleep(0.06)   

    elif kontrol(["mustafa"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(mustafa)
        await asyncio.sleep(0.06)        

    elif kontrol(["arkadaş","arkadas"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(arkadaş)
        await asyncio.sleep(0.06)         

    elif kontrol(["sus","suss","suus"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sus)
        await asyncio.sleep(0.06)          

    elif kontrol(["üzüldüm","üşüldüm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(üzüldüm)
        await asyncio.sleep(0.06)  

    elif kontrol(["kötü"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(kötü)
        await asyncio.sleep(0.06)   

    elif kontrol(["akşamlar"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(akşamlar)
        await asyncio.sleep(0.06)   

    try:
        await msg.reply(reply)
    except Exception as e:
        print(e)

    msg.continue_propagation()  #! BURAYA DOKUNMA
