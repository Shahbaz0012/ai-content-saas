from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import models
from app.services.openai_service import generate_content
from app.routers import content, auth

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Content Generator API",
    version="0.7.0"
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(content.router)
app.include_router(auth.router)


class GenerateRequest(BaseModel):
    prompt: str
    content_type: str = "blog"
    tone: str = "professional"


@app.get("/")
def root():
    return {"message": "AI Content Generator API", "version": "0.7.0"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/api/generate")
async def create_content(
    request: GenerateRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(auth.get_current_user)
):
    # Check credits before generating
    user = db.query(models.User).filter(models.User.id == current_user["id"]).first()
    if user.credits <= 0:
        raise HTTPException(status_code=403, detail="No credits remaining. Please upgrade.")
    
    try:
        content = await generate_content(
            prompt=request.prompt,
            content_type=request.content_type,
            tone=request.tone
        )
        
        word_count = len(content.split())
        
        return {
            "content": content,
            "word_count": word_count,
            "content_type": request.content_type,
            "credits_remaining": user.credits
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))