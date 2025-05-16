from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
import os

# Environment variables থেকে API ডেটা নেওয়া
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
user_id = int(os.environ.get("USER_ID"))         # আপনার নিজের numeric Telegram user ID
group_id = os.environ.get("GROUP_ID")            # গ্রুপ username বা ID (ex: -1001234567890)

# Telethon ক্লায়েন্ট তৈরি
client = TelegramClient("session", api_id, api_hash)

# 15টি রিয়েক্ট ইমোজি
reactions = [
    '❤️', '🔥', '👍', '😍', '😱', '👏', '💯',
    '❤️‍🔥', '🎉', '🤩', '', '👌🏻', '🗿', '⚡'
]

# নতুন মেসেজ এলে এবং আপনি পোস্ট করলে রিয়েক্ট দিবে
@client.on(events.NewMessage(chats=group_id))
async def react(event):
    if event.sender_id == user_id:
        await client(SendReactionRequest(
            peer=event.chat_id,
            msg_id=event.id,
            reaction=reactions
        ))

# Render ping এর জন্য /ping কমান্ড
@client.on(events.NewMessage(pattern="/ping"))
async def ping(event):
    await event.reply("I'm alive!")

# বট চালু করা
client.start()
client.run_until_disconnected()
