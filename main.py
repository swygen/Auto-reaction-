from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
import os
import asyncio

# Environment variables থেকে API ডেটা নেওয়া
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
user_id = int(os.environ.get("USER_ID"))         # আপনার নিজের numeric Telegram user ID
group_id = os.environ.get("GROUP_ID")            # গ্রুপ username বা ID (ex: -1001234567890)

# Telethon ক্লায়েন্ট তৈরি
client = TelegramClient("session", api_id, api_hash)

# রিয়েক্ট ইমোজির লিস্ট (খালি স্ট্রিং বাদ দেওয়া হয়েছে)
reactions = [
    '❤️', '🔥', '👍', '😍', '😱', '👏', '💯',
    '❤️‍🔥', '🎉', '🤩', '👌🏻', '🗿', '⚡'
]

@client.on(events.NewMessage(chats=group_id))
async def react(event):
    if event.sender_id == user_id:
        for reaction in reactions:
            try:
                await client(SendReactionRequest(
                    peer=event.chat_id,
                    msg_id=event.id,
                    reaction=reaction
                ))
                await asyncio.sleep(0.3)  # একটু সময় দিব যাতে স্প্যাম মনে না হয়
            except Exception as e:
                print(f"Failed to send reaction {reaction}: {e}")

@client.on(events.NewMessage(pattern="/ping"))
async def ping(event):
    await event.reply("I'm alive!")

# বট চালু করা
client.start()
client.run_until_disconnected()
