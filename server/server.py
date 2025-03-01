import os

from dotenv import load_dotenv
from telethon import TelegramClient, events, functions
import json

load_dotenv()

api_id = os.getenv('BOT_ID')
api_hash = os.getenv('BOT_HASH')

channels_to_id = json.loads(os.getenv('CHANNELS_TO_ID'))
topics_to_id = json.loads(os.getenv('TOPIKS_TO_ID'))
channels = json.loads(os.getenv('CHANNELS_FROM_ID'))

for i in range(len(channels)):
    if channels[i][0]!="@":
        channels[i] = int(channels[i])

for i in range(len(topics_to_id)):
    if topics_to_id[i][0]!="@":
        topics_to_id[i] = int(topics_to_id[i])      

for i in range(len(channels_to_id)):
    if channels_to_id[i][0]!="@":
        channels_to_id[i] = int(channels_to_id[i])      
        
client = TelegramClient('swgohbot', api_id, api_hash)
print("Bot - started")

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    if event.message:
        for channel_to, topics_to in zip(channels_to_id, topics_to_id):
            # await client.send_message(channel_to, event.message,  reply_to=topics_to)
            await client(functions.messages.ForwardMessagesRequest(
            from_peer=event.chat.id,     # <- chat where the messages exist
            id=[event.message.id],             # <- message ids to forward from source_chat
            to_peer=channel_to,  # <- where to forward the messages
            top_msg_id=topics_to,       # <- topic id
        ))

client.start()
client.run_until_disconnected()
