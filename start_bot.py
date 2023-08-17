from pyrogram import Client

import config

api_id = config.api_id
api_hash = config.api_hash
bot_token = config.token

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()
