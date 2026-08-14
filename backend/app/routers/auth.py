from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.utils.security import get_password_hash, verify_password, create_access_token
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/auth", tags=["auth"])


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    # Check if user exists
    existing = db.query(models.User).filter(models.User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create user
    hashed = get_password_hash(data.password)
    user = models.User(email=data.email, hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return {"message": "User created", "user_id": user.id, "email": user.email}


@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    token = create_access_token({"sub": str(user.id), "email": user.email})
    return {"access_token": token, "token_type": "bearer"}