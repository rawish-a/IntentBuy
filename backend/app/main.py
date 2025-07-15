from fastapi import FastAPI
from app.routers import auth as auth_router  # import your auth routes
from app.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from sqlalchemy import text
from app.routers import posts as posts_router

app = FastAPI()

app.include_router(posts_router.router)



@app.get("/")
async def root():
    return {"message": "IntentBuy backend is running"}

# Optional: Test DB connection using async SQLAlchemy session
@app.get("/users/")
async def get_users(db: AsyncSession = Depends(get_async_session)):
    result = await db.execute(text("SELECT * FROM users"))
    users = result.mappings().all()  # returns list of dict-like rows
    return users

# Register auth routes
app.include_router(auth_router.router)
