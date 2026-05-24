import asyncio
from database.db import init_db
from aiogram import Bot , Dispatcher
from dotenv import load_dotenv
import os
from handlers import greeting , settings

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main_function():
    await init_db()

    dp.include_router(greeting.router)
    dp.include_router(settings.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main_function())