from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str
    password: str  

class UserLogin(BaseModel):
    username : str
    password : str
    
    
class Token(BaseModel):
    access_token : str
    token_type : str
    
    
class TokenData(BaseModel):
    id: Optional[str] = None