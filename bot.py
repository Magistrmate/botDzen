from pyrogram import Client, filters
import config

bot = Client('my_bot')


# @bot.on_message(filters.text & filters.private)
# async def echo(client, message):
#     await message.reply(message.text)


@bot.on_chat_member_updated(filters.chat(config.chat_group))
def okay(client, chat_member_update):
    print(client, chat_member_update)


@bot.on_user_status(filters.chat(config.chat_group))
def new_channel_post(client, user):
    print(client, user)


bot.run()
