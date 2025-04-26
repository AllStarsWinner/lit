import aiosqlite

DATABASE = "database.db"

async def init_db():
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE, 
                name TEXT,
                surname TEXT,
                age INTEGER,
                nomer TEXT,
                question TEXT
            )
        """)
        await db.commit()

async def add_user(user_id: int, name: str, surname: str, age: int, nomer: str, question: str):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("INSERT OR IGNORE INTO users (user_id, name, surname, age, nomer, question) VALUES(?, ?, ?, ?, ?, ?)",
                         (user_id, name, surname, age, nomer, question))
        await db.commit()

async def get_user():
    async with aiosqlite.connect(DATABASE) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()
