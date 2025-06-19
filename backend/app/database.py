from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from databases import Database
from fastapi import Depends
from app.config import settings

# Load DB URL from .env
DATABASE_URL = settings.database_url

# Used by `databases` package (optional depending on your stack)
database = Database(DATABASE_URL)

# SQLAlchemy engine
engine = create_async_engine(DATABASE_URL, echo=True)

# SQLAlchemy async session maker
async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# FastAPI dependency to inject session into routes
async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session
