from databases import Database

DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/intentbuy_db"

database = Database(DATABASE_URL)