from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
import os
import asyncio

# Environment variables থেকে API ডেটা নেওয়া
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
phone = os.environ.get("PHONE")                   # ফোন নাম্বার environment থেকে নিবে
user_id = int(os.environ.get("USER_ID"))          # আপনার নিজের numeric Telegram user ID
group_id = os.environ.get("GROUP_ID")             # গ্রুপ username বা ID (ex: -1001234567890)

# Telethon ক্লায়েন্ট তৈরি
client = TelegramClient("session", api_id, api_hash)

# রিয়েক্ট ইমোজির লিস্ট
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
                await asyncio.sleep(0.3)  # স্প্যাম এড়াতে সামান্য সময় দিবে
            except Exception as e:
                print(f"Failed to send reaction {reaction}: {e}")

@client.on(events.NewMessage(pattern="/ping"))
async def ping(event):
    await event.reply("I'm alive!")

async def keep_alive():
    while True:
        try:
            # প্রতি ৫ মিনিটে বটের স্ট্যাটাস চেক করার জন্য ping event ইমিট করা বা কনসোল লগ
            print("Keep alive ping...")
            await asyncio.sleep(300)  # ৫ মিনিট = 300 সেকেন্ড
        except Exception as e:
            print(f"Keep alive error: {e}")
            await asyncio.sleep(10)

async def main():
    await client.start(phone=phone)
    # keep_alive টাস্ক শুরু
    asyncio.create_task(keep_alive())
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
