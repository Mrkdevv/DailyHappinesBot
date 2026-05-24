import aiosqlite
import asyncio


async def init_db():
    db = await aiosqlite.connect('TelegramDateBase.db')

    #Create Cursor
    cursor = await db.cursor()

    await cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        message_time TEXT
        )
        """)
    await cursor.execute("""CREATE TABLE IF NOT EXISTS mood_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date TEXT,
        score INTEGER,
        comment TEXT
        )
    """)

    await db.commit()

    await cursor.close()
    await db.close()

async def add_user(user_id: int):
    async with aiosqlite.connect('TelegramDateBase.db') as db:
         async with db.cursor() as cursor:
            await cursor.execute("INSERT OR IGNORE INTO users (user_id , message_time) VALUES (?, NULL) ",(user_id,) )
            await db.commit()

async def add_time(user_id: int , time_str: str):
    async with aiosqlite.connect('TelegramDateBase.db') as db:
        async with db.cursor() as cursor:
            await cursor.execute("UPDATE users SET message_time = ? where user_id = ?",(time_str,user_id) )
            await db.commit()

if __name__ == "__main__":
    asyncio.run(init_db())