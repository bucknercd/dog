import sys
from datetime import timedelta
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


router = APIRouter()

templates = Jinja2Templates(directory="app/templates")



@router.get(
            '/register',
            tags=["authentication"],
            status_code=200
)
async def register(request: Request, invalid: bool = False):
    return templates.TemplateResponse('register.html', {'request': request, 'title': 'Register', 'invalid': invalid})

@router.post(
            '/register',
            tags=["authentication"],
            response_model=UserResponse,
            status_code=201
)
async def register(user: UserRegister):
    dbuser = get_user(username=user.username)
    if dbuser:
        raise HTTPException(status_code=404, detail="User already exists in database.")
    _id = create_user(user)
    if not _id:
        raise HTTPException(status_code=404, detail="Unable to create the user.")
    dbuser = get_user(username=user.username)
    if dbuser:
        return UserResponse(**dbuser.dict())
    else:
        raise HTTPException(status_code=404, detail="User was not created upon registration.")
    
    

@router.get(
            '/login',
            tags=["authentication"],
)
async def login(request: Request, invalid: bool = False):
    return templates.TemplateResponse('login.html', {'request':request, 'title': 'Sign In', 'invalid': invalid})

@router.post(
            '/login',
            tags=["authentication"],
            status_code=200,
            response_model=LoginResponse,
)
async def login(request: Request,
                response: Response,
                login: UserLogin,
): # session_id: str = Cookie(None)
    # goal: return a UserResponse object
    # get UserDB from db using username
    # get user id from object
    # check for a session cookie in req header
    # cookie?
    #   check db in collection cookies for a valid session cookie (not expired) using cookie in header
    #   valid cookie? ( time not expired)
    #     return UserResponse crafted from UserDB
    #   invalid cookie or no cookie? ( time expired)
    #     verify password with salt and hash from UserDB obj
    #     create a new cookie and insert in db
    #     add this cookie to resp header
    #     return UserResponse crafted from UserDB
    #
    user, session_cookie = login_user(login.username, login.password, login.remember_me)        
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username and/or password.")
    login_dict = user.dict()
    login_dict['cookie'] = session_cookie.dict()
    print(f'login dict: LoginResponse => {login_dict}')
    return LoginResponse(**login_dict)

