import asyncio
import logging
from os import environ
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import bot_token


logging.basicConfig(level=logging.INFO)
if isinstance(bot_token,str):
    bot = Bot(token=bot_token)
else:
    BOT_TOKEN = environ["BOT_TOKEN"]
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer("Hello!")


@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ c "ответом"')


@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    print(bot_token)
