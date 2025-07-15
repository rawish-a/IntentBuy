from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, models, crud
from app.database import get_async_session
from app.routers.auth import get_current_user  # adjust path if needed

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=schemas.InfluencerPostOut, status_code=201)
async def create_post(
    post: schemas.InfluencerPostCreate,
    current_user: models.User = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.create_influencer_post(db, post, current_user.id)

@router.get("/", response_model=list[schemas.InfluencerPostOut])
async def list_my_posts(
    skip: int = 0,
    limit: int = 20,
    current_user: models.User = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.get_posts_for_user(db, current_user.id, skip, limit)
