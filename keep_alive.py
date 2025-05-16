import asyncio

async def keep_alive():
    while True:
        print("Keep alive ping...")
        await asyncio.sleep(300)  # ৫ মিনিট অপেক্ষা করবে

if __name__ == "__main__":
    asyncio.run(keep_alive())
