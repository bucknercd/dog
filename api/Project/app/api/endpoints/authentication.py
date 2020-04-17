from datetime import timedelta

from fastapi import APIRouter#, Body, Depends
#from starlette.exceptions import HTTPException

#from ....core.config import ACCESS_TOKEN_EXPIRE_MINUTES
#from ....core.jwt import create_access_token
#from ....crud.shortcuts import check_free_username_and_email
#from ....crud.user import create_user, get_user_by_email
from ...db.mongodb import conn
from ...models.users import UserRegister


router = APIRouter()


# 
@router.post('/register', status_code=200)
async def register(user: str):
    # goals: 
        # create a user in db
            # create a user obj ( a dict)
            # insert user obj into db
            # create_user()
            # login()
    #users.create_user


    #user = '{"name": "Gabriel Buckner", "age": 0}'
    #conn.insert(user, 'users')
    return user
