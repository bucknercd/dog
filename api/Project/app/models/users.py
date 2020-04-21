from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserRegister(BaseModel):
    username: str
    password: str
    password_hash: str
    email: EmailStr = None
    full_name: str
    dogs: list
    zip_code: int
    phone_number: int
    user_id: int = 0

class UserLoginResponse(BaseModel):
    full_name: str
    user_id: str


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None
