from main import dp
from aiogram.filters.command import Command
from aiogram import types


@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer("Привет! Я бот-ассистент для отображения расписания поездов.")
