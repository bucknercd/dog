from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserRegister(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None
