import asyncio
from pyrogram import Client
import config

api_id = config.api_id
api_hash = config.api_hash


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
