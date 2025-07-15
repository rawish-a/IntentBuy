from sqlalchemy import Column, String, Text, Boolean, DateTime, Float, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<User id={self.id} email={self.email}>"


class InfluencerPost(Base):
    __tablename__ = "influencer_posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    post_url = Column(Text, nullable=False)
    caption_text = Column(Text)

    promo_detected = Column(Boolean, default=False)
    confidence_score = Column(Float)

    creator_username = Column(String, nullable=False)
    creator_known = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
