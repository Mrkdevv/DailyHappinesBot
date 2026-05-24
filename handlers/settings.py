from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart, callback_data
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.db import add_user , add_time
import asyncio

router = Router()

TIMES = ["17:00" , "18:00" , "19:00" , "20:00" , "21:00" , "22:00" , "23:00" , "00:00"]

@router.message(Command("settings"))
async def settings(message: Message):
    builder = InlineKeyboardBuilder()
    for time_str in TIMES:
        builder.button(text=time_str, callback_data=f"set_time:{time_str}")

    builder.adjust(4)

    await message.answer(
        "Выбери удобное время для ежедневного опроса о твоем настроении:",
        reply_markup=builder.as_markup()
    )

@router.callback_query(F.data.startswith(f"set_time:"))
async def process_time_selection(callback: CallbackQuery):
    selected_time = callback.data.split(":")[1]
    user_id = callback.from_user.id
    await add_time(user_id , selected_time)

    await callback.answer()


    await callback.message.edit_text(
        f"✅ Время успешно установлено на {selected_time}:00!\n"
        f"Каждый день в это время я буду спрашивать тебя о настроении."
    )