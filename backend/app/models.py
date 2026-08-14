# Database table models
# Defines the structure of database tables

from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    """User account table"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, nullable=True)
    plan = Column(String, default="free")      # free, pro
    credits = Column(Integer, default=5)         # free users get 5 credits
    created_at = Column(DateTime, server_default=func.now())


class Content(Base):
    """Generated content history table"""
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    content_type = Column(String, nullable=False)  # blog, social, ad, email
    prompt = Column(Text, nullable=False)          # what user typed
    output = Column(Text, nullable=False)          # what AI generated
    word_count = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now())