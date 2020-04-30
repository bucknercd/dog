from datetime import timedelta
from fastapi import APIRouter, Cookie#, Body, Depends
#from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
#from ....core.config import ACCESS_TOKEN_EXPIRE_MINUTES
#from ....core.jwt import create_access_token
#from ....crud.shortcuts import check_free_username_and_email
#from ....crud.user import create_user, get_user_by_email

from ...db.mongodb import conn
from ...models.users import UserRegister, UserResponse, UserLogin
from ...crud.users import create_user, login_user, get_user


router = APIRouter()

@router.post(
            '/register',
            response_model=UserResponse,
            tags=["authentication"],
            status_code=HTTP_201_CREATED
)
async def register(user: UserRegister):
    print(f'{user}')
    # goals: 
        # create a user in db
            # create a user obj ( a dict)
            # insert user obj into db
            # get a user id! -- research here
            # create_user()
            # login()
    _id = create_user(user)
    print(f'_id: {_id}')

    #session_id = login_user(user.username, user.password)
    #user = get_user(_id=_id)

    #user_out = UserResponse(**user.dict())
    #user_out.full_name = user.full_name
    #return user_out

@router.post(
            '/login',
            response_model=UserResponse,
            tags=["authentication"],
)
async def login(user: UserLogin, session_id: str = Cookie(None)):
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
    dbuser = get_user(user.username)


