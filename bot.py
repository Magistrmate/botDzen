import config
import sqlite3

from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=config.token)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
    print('ok')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
