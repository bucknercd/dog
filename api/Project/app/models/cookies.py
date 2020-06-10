from pydantic import BaseModel
from typing import List
import enum

class Type(enum.Enum):
    session = 1

class Cookie(BaseModel):
    _type: int
    key: str
    value: str
    user_id: str
    create_date: str
    remember_me: bool = False