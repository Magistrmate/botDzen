from pyrogram import Client
import sqlite3
import config

app = Client('my_account')
conn = sqlite3.connect('users.db')
cursor = conn.cursor()


async def main():
    async with app:
        async for member in app.get_chat_members(config.chat_dzen):
            if member.user.is_self is False:
                user_id = member.user.id
                username = member.user.username
                join_date = member.joined_date
                cursor.execute('INSERT INTO users (user_id, username, join_date) VALUES (?,?,?)', (user_id,
                                                                                                   username, join_date))
        conn.commit()
        print(member.joined_date)

app.run(main())
