import sys
from datetime import timedelta
from pydantic import ValidationError
from fastapi import APIRouter, Request, Cookie, Response#, Body, Depends
from starlette.exceptions import HTTPException
from starlette.templating import Jinja2Templates
from starlette.status import HTTP_400_BAD_REQUEST
from starlette.responses import RedirectResponse
#from ....core.config import ACCESS_TOKEN_EXPIRE_MINUTES
#from ....core.jwt import create_access_token
#from ....crud.shortcuts import check_free_username_and_email
#from ....crud.user import create_user, get_user_by_email

from ...db.mongodb import conn
from ...models.users import UserRegister, UserResponse, UserLogin, LoginResponse
from ...crud.users import create_user, login_user, get_user
from ...crud.cookies import get_cookie

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get(
            '/users/{session_id}',
            tags=["users"],
            status_code=200,
            response_model=LoginResponse,
)
async def get_a_user(session_id: str, response: Response):
    # cast to type LoginResponse!
    user = get_user(session_cookie=session_id)
    cookie = get_cookie(session_id)
    print(f'username: {user.username}')
    # cast to type LoginResponse!
    user_dict = user.dict()
    user_dict.update({'cookie': cookie})
    print(f'user dict: {user_dict}')
    if user:
        return LoginResponse(**user_dict)
    else:
        raise HTTPException(status_code=404, detail="User was not found.")
