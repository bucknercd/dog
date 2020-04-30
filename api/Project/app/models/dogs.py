from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import enum

app = FastAPI()


class Dog(BaseModel):
    name: str
    breed: str
    weight: int
    size: int
    rabies: bool
    heartworm: bool
    flea: bool
    behavior: str

class Size(enum.Enum):
    small = 1
    medium = 2
    large = 3
