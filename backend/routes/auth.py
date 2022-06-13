from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from config.utils import verify
from config.oauth2 import create_access_token
from passlib.context import CryptContext
from schemas.user import *




# postgre
from config.db import get_db
from sqlalchemy.orm import Session
from models.dbschema import User
from sqlalchemy import insert


authentication = APIRouter( prefix = "/users", tags=["users"])

pwd_context = CryptContext(schemes=["bcrypt"])


@authentication.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
 
    
    user = db.query(User.username, User.password).where(User.username == user_credentials.username).first()
    
    if not user:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not verify(user_credentials.password, user.password):
         raise HTTPException(
             status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")


    access_token = create_access_token(data={"username": user.username})

    return {"access_token": access_token, "token_type": "bearer"}


def get_password_hash(password):
     return pwd_context.hash(password)


@authentication.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserRegister, db : Session = Depends(get_db)):
    
    all_users = db.query(User).all()
    
    if any(x.username == user.username for x in all_users):
        raise HTTPException(400, 'user name is taken')

    hashed_password = get_password_hash(user.password)
    
    
    insert_stmt = insert(User).values(
        username = user.username,
        password = hashed_password
    )
    
    db.execute(insert_stmt)
    db.commit()
    
    return db.query(User.username, User.password).where(User.username == user.username).all()

