from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

from schemas.user import TokenData
from config.env import settings

from sqlalchemy.orm import Session
from config.db import get_db


# postgre
from config.db import get_db
from sqlalchemy.orm import Session
from models.dbschema import *



oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


# This would generate a token
# More detail - https://jwt.io/

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(days=settings.ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return encoded_jwt

# This function will verify the access token
def verify_access_token(token: str, credentials_exception):

    try:

        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        id: str = payload.get("username")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data


# This is a function that will be put in the api call to provide a security
# layer whenever an api is called.
def get_current_user(token: str = Depends(oauth2_scheme), db : Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials", 
                                          headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)
    
    
    #user = conn.execute(dbUsers.select().where(dbUsers.c.username == token.id)).first()
    user  = db.query(User).where(User.username == token.id).first()
    
    return user