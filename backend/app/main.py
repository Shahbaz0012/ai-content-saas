# Main FastAPI application entry point
# Milestone 1: Basic server with health check endpoint

from fastapi import FastAPI

# Initialize FastAPI application
app = FastAPI(
    title="AI Content Generator API",
    description="Backend API for AI-powered content generation SaaS",
    version="0.1.0"
)

# Root endpoint - confirms API is running
@app.get("/")
def root():
    return {
        "message": "AI Content Generator API is running",
        "status": "ok",
        "version": "0.1.0"
    }

# Health check endpoint for monitoring
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }