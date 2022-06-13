from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from config.db import conn
from config.utils import verify
from config.oauth2 import create_access_token
from passlib.context import CryptContext
from schemas.user import UserLogin, User
from models.dbschema import dbUsers


authentication = APIRouter( 
          prefix = "/users",
          tags=["users"]
          )


pwd_context = CryptContext(schemes=["bcrypt"])


@authentication.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
# def login(user_credentials: UserLogin):
 
    # Get user details from database
    user = conn.execute(dbUsers.select().where(dbUsers.c.username == user_credentials.username)).first()

    if not user:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not verify(user_credentials.password, user.password):
         raise HTTPException(
             status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")


    # This would generate a token
    # More detail - https://jwt.io/
    access_token = create_access_token(data={"username": user.username})

    return {"access_token": access_token, "token_type": "bearer"}


def get_password_hash(password):
     return pwd_context.hash(password)


# This API will register material planner and overwrite FastAPI default status - status.HTTP_200_OK
@authentication.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: User):
    all_users = conn.execute(dbUsers.select()).fetchall()
    if any(x['username'] == user.username for x in all_users):
        raise HTTPException(400, 'user name is taken')

    hashed_password = get_password_hash(user.password)

    conn.execute(dbUsers.insert().values(   
        username=user.username,
        password=hashed_password
    ))

    return conn.execute(dbUsers.select().where(dbUsers.c.username == user.username)).fetchall()