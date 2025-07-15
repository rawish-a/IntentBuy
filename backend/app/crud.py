from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User
from app.auth import hash_password, verify_password
from typing import List
from app.schemas import InfluencerPostCreate  
from app.models import InfluencerPost
import uuid

# Get user by email
async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()

# Register a new user
async def create_user(db: AsyncSession, email: str, password: str):
    user = User(email=email, hashed_password=hash_password(password))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

# Authenticate user (for login)
async def authenticate_user(db: AsyncSession, email: str, password: str):
    user = await get_user_by_email(db, email)
    if user and verify_password(password, user.hashed_password):
        return user
    return None

# ---------- Influencer Posts ---------- #
async def create_influencer_post(
    db: AsyncSession,
    post_in: InfluencerPostCreate,
    user_id: uuid.UUID
):
    post = InfluencerPost(user_id=user_id, **post_in.model_dump())
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post

async def get_posts_for_user(
    db: AsyncSession,
    user_id: uuid.UUID,
    skip: int = 0,
    limit: int = 20
) -> List[InfluencerPost]:
    result = await db.execute(
        select(InfluencerPost)
        .where(InfluencerPost.user_id == user_id)
        .offset(skip).limit(limit)
    )
    return result.scalars().all()