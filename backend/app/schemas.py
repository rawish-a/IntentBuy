from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, constr, HttpUrl, Field

# -----------------  User Schemas  -----------------

class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=6, max_length=64)

class UserOut(BaseModel):
    id: int            # users.id is INTEGER in the DB
    email: EmailStr

    class Config:
        orm_mode = True


# -----------------  Auth Token  -----------------

class Token(BaseModel):
    access_token: str
    token_type: str


# -----------------  Influencer Post Schemas  -----------------

class InfluencerPostBase(BaseModel):
    post_url: HttpUrl                          # validates full URL
    caption_text: str | None = None
    promo_detected: bool
    confidence_score: float | None = Field(
        None, ge=0.0, le=1.0, description="0‑1 confidence score"
    )
    creator_username: str
    creator_known: bool

class InfluencerPostCreate(InfluencerPostBase):
    """Payload a client sends to create a post scan."""
    pass

class InfluencerPostOut(InfluencerPostBase):
    """Data the API returns."""
    id: UUID
    user_id: int                              # FK matches users.id (integer)
    created_at: datetime

    class Config:
        orm_mode = True
