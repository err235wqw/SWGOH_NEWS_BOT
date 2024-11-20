import os

from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()
api_id = os.getenv('BOT_ID')
api_hash = os.getenv('BOT_HASH')

my_channel_id = int(os.getenv('CHANNEL_ID'))
topic_id = int(os.getenv('TOPIK_ID'))
client = TelegramClient('swgohbot', api_id, api_hash)
print("Bot - started")
channels = ["@rus_swgoh", '@tetetetsadgf']


@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    if event.message:
        await client.send_message(my_channel_id, event.message,  reply_to=topic_id)

client.start()
client.run_until_disconnected()
