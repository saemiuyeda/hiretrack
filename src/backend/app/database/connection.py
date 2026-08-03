from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5432/database"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False, bind= engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()