from pydantic import BaseModel, EmailStr, constr
from uuid import UUID
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=6, max_length=64)

class UserOut(BaseModel):
    id: UUID
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class InfluencerPostBase(BaseModel):
    post_url: str
    caption_text: str | None = None
    promo_detected: bool
    confidence_score: float | None = None
    creator_username: str
    creator_known: bool

class InfluencerPostCreate(InfluencerPostBase):
    pass                                  # everything required for creation

class InfluencerPostOut(InfluencerPostBase):
    id: UUID
    user_id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
