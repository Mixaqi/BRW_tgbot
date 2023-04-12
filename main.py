import asyncio
import logging
from os import environ
from aiogram import Bot, Dispatcher
from data.config_reader import bot_token
from handlers.users import slash_commands



logging.basicConfig(level=logging.INFO)
if isinstance(bot_token, str):
    bot = Bot(token=bot_token, parse_mode="HTML")
else:
    BOT_TOKEN = environ["BOT_TOKEN"]
dp = Dispatcher()


async def main() -> None:
    await dp.start_polling(bot)
    slash_commands.cmd_start()

if __name__ == "__main__":
    asyncio.run(main())

