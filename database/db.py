import aiosqlite
import asyncio


async def init_db():
    db = await aiosqlite.connect('TelegramDateBase.db')

    #Create Cursor
    cursor = await db.cursor()

    await cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        massage_time TEXT
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


if __name__ == "__main__":
    asyncio.run(init_db())