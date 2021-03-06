from pydantic import BaseModel, EmailStr
from typing import List
from .dogs import Dog
from .cookies import Cookie

class BaseUser(BaseModel):
    username: str
    email: EmailStr = None
    full_name: str
    dogs: List[Dog]
    zip_code: int
    phone_number: int = 0

# user data to be returned to user from api
class UserResponse(BaseUser):
    user_id: str = None

# register data coming from user and to be used in api as well
class UserRegister(BaseUser):
    password: str

# user data to be inserted in db
class UserDB(UserResponse):
    password_hash: str = None
    password_salt: str = None

class UserLogin(BaseModel):
    username: str
    password: str
    remember_me: bool = False

class LoginResponse(UserResponse):
    cookie: Cookie