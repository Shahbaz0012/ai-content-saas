from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from app.database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    credits = Column(Integer, default=5)
    created_at = Column(DateTime, default=datetime.utcnow)


class ContentHistory(Base):
    __tablename__ = "content_history"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    prompt = Column(Text)
    content_type = Column(String)
    tone = Column(String)
    generated_content = Column(Text)
    word_count = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)