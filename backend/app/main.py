from fastapi import FastAPI
from .database import database
from .config import settings

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Testing"}

@app.get("/users/")
async def get_users():
    query = "SELECT * FROM users;"
    results = await database.fetch_all(query)
    return results

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()