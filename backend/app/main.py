from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.database import Base, engine
from app import models
from app.services.openai_service import generate_content
from app.routers import content

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Content Generator API",
    version="0.4.0"
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include content router
app.include_router(content.router)


class GenerateRequest(BaseModel):
    prompt: str
    content_type: str = "blog"
    tone: str = "professional"


@app.get("/")
def root():
    return {"message": "AI Content Generator API", "version": "0.4.0"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/api/generate")
async def create_content(request: GenerateRequest):
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
            "content_type": request.content_type
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))