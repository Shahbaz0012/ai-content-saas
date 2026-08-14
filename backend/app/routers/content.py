from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.utils.security import get_current_user
from pydantic import BaseModel

router = APIRouter(prefix="/api/content", tags=["content"])


class ContentSaveRequest(BaseModel):
    prompt: str
    content_type: str
    tone: str
    generated_content: str
    word_count: int


@router.post("/save")
def save_content(
    data: ContentSaveRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    # Check credits
    user = db.query(models.User).filter(models.User.id == current_user["id"]).first()
    if user.credits <= 0:
        raise HTTPException(status_code=403, detail="No credits remaining. Please upgrade.")
    
    # Deduct 1 credit
    user.credits -= 1
    db.commit()
    
    # Save content
    db_content = models.ContentHistory(
        user_id=current_user["id"],
        prompt=data.prompt,
        content_type=data.content_type,
        tone=data.tone,
        generated_content=data.generated_content,
        word_count=data.word_count
    )
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    
    return {
        "message": "Content saved",
        "id": db_content.id,
        "credits_remaining": user.credits
    }


@router.get("/history")
def get_history(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    history = db.query(models.ContentHistory).filter(
        models.ContentHistory.user_id == current_user["id"]
    ).order_by(models.ContentHistory.created_at.desc()).all()
    return history


@router.get("/credits")
def get_credits(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    user = db.query(models.User).filter(models.User.id == current_user["id"]).first()
    return {"credits": user.credits, "max_credits": 5}