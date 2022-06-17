import psycopg2
from psycopg2.extras import RealDictCursor
import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.env import settings


#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root123@localhost/postgres"

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DATABASE}'
                                                                                                    
                                                                                                    
#.DB_USER, settings.DB_PASSWORD, settings.DB_HOST, settings.DB_PORT , settings.DATABASE)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

