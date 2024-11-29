#
# Copyright (C) 2021-2023 by ArchBots@Github, < https://github.com/ArchBots >.
#
# This file is part of < https://github.com/ArchBots/ArchMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/ArchBots/ArchMusic/blob/master/LICENSE >
#
# All rights reserved.
#

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from ArchMusic import LOGGER, app, userbot
from ArchMusic.core.call import ArchMusic
from ArchMusic.plugins import ALL_MODULES
from ArchMusic.utils.database import get_banned_users, get_gbanned, get_active_chats

loop = asyncio.get_event_loop_policy().get_event_loop()


async def auto_restart(interval_minutes):
    while True:
        await asyncio.sleep(interval_minutes * 60)
        await restart_bot()

async def restart_bot():
    served_chats = await get_active_chats()
    for x in served_chats:
        try:
            await app.send_message(
                x,
                f"**{config.MUSIC_BOT_NAME} kendini yeniden başlattı. Sorun için özür dileriz.\n\n10-15 saniye sonra yeniden müzik çalmaya başlayabilirsiniz.**",
            )
        except Exception:
            pass
    try:
        await app.send_message(
            config.LOG_GROUP_ID,
            f"**{config.MUSIC_BOT_NAME} kendini otomatik olarak yeniden başlatıyor.**",
        )
    except Exception:
        pass
    os.system(f"kill -9 {os.getpid()} && bash start")
    

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("ArchMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("ArchMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ArchMusic.plugins" + all_module)
    LOGGER("ArchMusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await ArchMusic.start()
    try:
        await ArchMusic.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("ArchMusic").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await ArchMusic.decorators()
    LOGGER("ArchMusic").info("Arch Music Bot Started Successfully")

    interval_minutes = 360
    asyncio.create_task(auto_restart(interval_minutes))

    
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("ArchMusic").info("Stopping Arch Music Bot! GoodBye")
