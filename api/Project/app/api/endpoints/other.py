from fastapi import APIRouter, HTTPException
from starlette.templating import Jinja2Templates
from starlette.requests import Request

from ...models.users import UserRegister, UserResponse

router = APIRouter()

@router.get('/user/{session_id}')
async def get_user(session_id: str):
    dbuser = get_user(session_cookie=session_id)
    if dbuser:
        return UserResponse(**dbuser.dict())
    else:
        raise HTTPException(status_code=404, detail="Unable to retrieve user.")
