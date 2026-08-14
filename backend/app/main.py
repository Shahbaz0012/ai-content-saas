# Main FastAPI application

from fastapi import FastAPI

from app.database import Base, engine
from app import models

# Create database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Content Generator API",
    description="Backend API for AI-powered content generation SaaS",
    version="0.2.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Content Generator API is running",
        "status": "ok",
        "version": "0.2.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "database": "connected"
    }