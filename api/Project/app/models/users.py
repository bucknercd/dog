from pydantic import BaseModel, EmailStr
from typing import List
from .dogs import Dog


# user data to be returned to user from api
class UserResponse(BaseModel):
    username: str
    email: EmailStr = None
    full_name: str
    dogs: List[Dog]
    zip_code: int
    phone_number: int

# register data coming from user and to be used in api as well
class UserRegister(UserResponse):
    password: str # not sure if needed

# user data to be inserted in db
class UserDB(UserResponse):
    password_hash: str
    password_salt: str

class UserLogin(BaseModel):
    username: str
    email: EmailStr = None
    password: str
