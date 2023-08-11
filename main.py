from pyrogram import Client
import sqlite3

import config

# Target channel/supergroup
TARGET = -1001859981405

app = Client("my_account")

conn = sqlite3.connect('users.db')
cursor = conn.cursor()


async def main():
    async with app:
        async for member in app.get_chat_members(config.chat_dzen):
            user_id = member.user.id
            username = member.user.username
            join_date = member.joined_date
            cursor.execute('INSERT INTO users (user_id, username, join_date) VALUES (?,?, ?)', (user_id,
                                                                                                username, join_date))
            conn.commit()
            # print(member.joined_date)


app.run(main())
