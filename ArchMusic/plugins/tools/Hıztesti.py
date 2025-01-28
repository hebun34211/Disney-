import io

from pyrogram import filters
from ArchMusic import app
import asyncio
import speedtest
from pyrogram import Client, filters
from pyrogram.types import Message



def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**Hız Testi Başladı**")
        test.download()
        m = m.edit("**Hız Testi Yükleniyor..**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**Hız Testi Tamamlandı**")
    except Exception as e:
        return m.edit(e)
    return result


@Client.on_message(filters.command(["hiz", "speedtest"]))


async def speedtest_function(client: Client, message: Message):
    m = await message.reply_text("Hız tesi başlatılıyor...")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**Speedtest Sonuçları**
    
<u>**İstemci:**</u>
**__ISP:__** {result['client']['isp']}
**__Şehir:__** {result['client']['country']}
  
<u>**Sunucu:**</u>
**__isim:__** {result['server']['name']}
**__Şehir:__** {result['server']['country']}, {result['server']['cc']}
**__Sponsor:__** {result['server']['sponsor']}
**__Ping:__** {result['ping']}"""
    msg = await client.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
