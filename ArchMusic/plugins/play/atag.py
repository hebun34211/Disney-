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


import os

import random


 


commandList = [

    "dice",

    "zar",

    "dart",

    "basketball",

    "basket" "football",

    "futbool",

    "gol",

    "bowling",

    "slot",

    "coin",

    "roll",

    "joke",

    "saka",

]



async def games(c: Client, m: Message):

    "🎲", "🎯", "🏀", "⚽", "🎳", "🎰"



    command = m.command[0]



    if command == "dice" or command == "zar":

        return await c.send_dice(m.chat.id, emoji="🎲")



    elif command == "dart" or command == "basketball":

        return await c.send_dice(m.chat.id, emoji="🎯")



    elif command == "basket":

        return await c.send_dice(m.chat.id, emoji="🏀")



    elif command == "football" or command == "futbool" or command == "gol":

        return await c.send_dice(m.chat.id, emoji="⚽")



    elif command == "bowling":

        return await c.send_dice(m.chat.id, emoji="🎳")



    elif command == "slot":

        return await c.send_dice(m.chat.id, emoji="🎰")



    elif command == "coin":

        return await m.reply(

            "**Yazı 🪙**" if random.randint(0, 1) == 0 else "**Tura 🪙**"

        )



    elif command == "roll":

        return await m.reply("**Uğurlu Rakamınız:** `{}`".format(random.randint(0, 9)))



    elif command == "joke" or command == "saka":

        return await m.reply_text(random.choice(jokes))



    return





slapMessages = [

    "{}, {}'nin RTX 2080Ti'sini kırdı!",

    "{}, {} üzerine benzin döktü ve ateşe verdi!",

    "{}, {}'nin kafasını bir balık dolu kovaya soktu",

    "{}, {}'nin yüzüne pasta fırlattı!",

    "{}, {}'nin yüzüne bir kahve döktü!",

    "{}, {}'nin yüzüne 150TL fırlattı!",

    "{}, {}'nin yüzüne bir çay döktü!",

    "{}, {}'nin yüzüne bir su döktü!",

    "{}, {} için aldığı hediyeyi parçaladı!",

    "{}, {}'nin yüzüne 200TL fırlattı!",

    "{}, {}'nin yüzüne bir kola döktü!",

    "{}, {} üzerine tüplü TV fırlattı!,",

    "{}, {}'nin kalbini kırdı!",

    "{}, {}'nin yüzüne bir kahve döktü!",

    "{}, {}'nin yüzüne 1TL fırlattı!",

    "{}, {}'nin yüzüne 5TL fırlattı!",

    "{}, {}'nin yüzüne 10TL fırlattı!",

    "{}, {}'nin yüzüne 20TL fırlattı!",

    "{}, {}'nin yüzüne 50TL fırlattı!",

    "{}, {}'nin yüzüne 100TL fırlattı!",

    "{}, {}'nin yüzüne 150TL fırlattı!",

    "{}, {}'nin yüzüne 200TL fırlattı!",

    "{}, {}'nin yüzüne bira döktü!",

    "{}, {}'nin yüzüne tokat attı!",

    "{}, {}'nin kafasını kesti!",

    "{}, {}'ye çicek verdi ",

    "{}, {}'nin yanağından öptü",

    "{}, {}'nin elinden tuttu ve dans etti",

    "{}, {}'nin agzına bir şeyler attı",

    "{}, {}'nin saçını çekti",

    "{}, {}'nin burnunu sıktı",

    "{}, {}'nin karnına tekme attı",

    "{}, {}'nin kafasına 💩 attı.",

    "{}, {}'nin yüzüne makyaj yaptı.",

    "{}, {}'nin yüzünü boyadı.",

    "{}, {}'nin saçını kesti.",

    "{}, {}'nin ayakkabısını çaldı.",

    "{}, {}'nin ayağına basarak yere düşürdü.",

    "{}, {}'nin ayağını gıdıkladı.",

]





@Client.on_message(filters.command("slap"))

@block

async def slap(bot: Client, message: Message):



    slapper = (

        "@" + message.from_user.username

        if message.from_user.username

        else message.from_user.mention

    )



    if message.reply_to_message:

        if not message.reply_to_message.from_user:

            return await message.reply_text("**Birini tokatlamak için yanıt verin!**")

        else:

            if message.reply_to_message.from_user.id == bot.me.id:

                return await message.reply_text("**Hey, beni tokatlama!**")

            else:

                slapped = (

                    "@" + message.reply_to_message.from_user.username

                    if message.reply_to_message.from_user.username

                    else message.reply_to_message.from_user.mention

                )

    else:

        slapper = "@" + BOT_USERNAME

        slapped = (

            "@" + message.from_user.username

            if message.from_user.username

            else message.from_user.mention

        )



    slapMessage = random.choice(slapMessages)



    await message.reply(slapMessage.format(slapper, slapped))

    return 
