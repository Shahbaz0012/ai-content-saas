# Database connection setup using SQLAlchemy
# SQLite is used for development (free, file-based, no installation needed)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL - creates a local file named contentgen.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./contentgen.db"

# Create database engine
# check_same_thread=False is required for SQLite to work with FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Session factory for database queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all database tables
Base = declarative_base()


# Function to get database session in API endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()