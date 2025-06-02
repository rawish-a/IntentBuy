from sqlalchemy.ext.asyncio import create_async_engine
from databases import Database
from app.config import settings

DATABASE_URL = settings.database_url

database = Database(DATABASE_URL)
engine = create_async_engine(DATABASE_URL)
