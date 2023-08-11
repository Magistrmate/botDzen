import config
import logging
import sqlite3

from aiogram import Bot, Dispatcher, executor, types

try:
    conn = sqlite3.connect('accountant.db')
    cursor = conn.cursor()

    cursor.execute("INSERT OR IGNORE INTO 'users' ('user_id') VALUES (?)", (1000,))

    users = cursor.execute("SELECT * FROM 'users'")
    print(users.fetchall())

    conn.commit()
    
except sqlite3.Error as error:
    print("Error", error)


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
