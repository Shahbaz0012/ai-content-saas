from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from pydantic import BaseModel

router = APIRouter(prefix="/api/content", tags=["content"])


class ContentSaveRequest(BaseModel):
    prompt: str
    content_type: str
    tone: str
    generated_content: str
    word_count: int


@router.post("/save")
def save_content(data: ContentSaveRequest, db: Session = Depends(get_db)):
    db_content = models.ContentHistory(
        user_id=1,  # temp user id
        prompt=data.prompt,
        content_type=data.content_type,
        tone=data.tone,
        generated_content=data.generated_content,
        word_count=data.word_count
    )
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return {"message": "Content saved", "id": db_content.id}


@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    history = db.query(models.ContentHistory).order_by(models.ContentHistory.created_at.desc()).all()
    return history