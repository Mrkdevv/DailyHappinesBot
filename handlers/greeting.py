import asyncio
from aiogram import Router, types
from aiogram.filters import CommandStart
from database.db import add_user

router = Router()

@router.message(CommandStart())
async def start(message: types.Message):
    user_id = message.from_user.id
    await add_user(user_id)
    await message.answer(
        "Привет! Я твой личный трекер счастья.\n"
        "Каждый день я буду спрашивать тебя о твоем настроении.\n"
        "Для начала давай настроим время уведомлений через /settings."
    )