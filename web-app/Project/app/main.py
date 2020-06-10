from fastapi import FastAPI, Response, Form
from starlette.templating import Jinja2Templates
from starlette.requests import Request
import requests
import json
from .models.users import UserRegister, UserResponse, UserLogin
from .core.config import API_HOSTNAME, UNIX_EPOCH_GMT

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

base_url = f'http://{API_HOSTNAME}/api'

@app.get('/')
async def get_index(request: Request):
    print(f'Cookie: {request.cookies.get("LS")}')
    print(f'from: {request.client}')
    print(f'http method: {request.method}')
    print(f'headers: {request.headers}')
    user_obj = {'request': request, 'title': 'home'}
    session_id = request.cookies.get('LS')
    if session_id:
        url = f'{base_url}/users/{session_id}'
        res = requests.get(url.encode())
        print(f'res json: {res.json()}')
        if res.status_code == 200:
            user_attrs = json.loads(res.json())
            user_obj.update(user_attrs)
    return templates.TemplateResponse('index.html', user_obj)

@app.get(
        '/register',
        status_code=201
)
async def register(request: Request):
    return templates.TemplateResponse('register.html', {'request': request, 'title': 'Register'})

@app.post(
            '/register',
            status_code=201
)
async def register(user: UserRegister, request: Request):
    url = f'{base_url}/register'
    user_obj = {'request': request}
    res = requests.post(url.encode(), data=user.json())
    if res.status_code == 201:
        user_attrs = json.loads(res.json())
        user_obj.update(user_attrs)
        user.obj.update({'title': 'home'})
        return templates.TemplateResponse('login.html', user_obj)
    else:
        user_obj.update({'title': 'register'})
        user_obj.update(user.dict())
        return templates.TemplateResponse('register.html', user_obj)
    
@app.get('/login',
        status_code=200,
)
async def login(request: Request):
    print(f'cookies (req): {request.cookies}')
    print(f'headers: {request.headers}')
    response = templates.TemplateResponse('login.html', {'request': request, 'title': 'login'})
    #response.delete_cookie('LS')
    response.set_cookie(key='LS', value='', expires=UNIX_EPOCH_GMT, httponly=True,secure=True)
    return response





@app.post(
         '/login',
         status_code=200
)
async def login(request: Request,
                username: str = Form(..., min_length=4, max_length=64),
                password: str = Form(..., min_length=8),
                remember_me: bool = False,
):
    user = UserLogin(username=username, password=password, remember_me=remember_me)
    url = f'{base_url}/login'
    user_obj = {'request': request}
    res = requests.post(url.encode(), data=user.json())
    if res.status_code == 200:
        print(f'login resp: {res.json()}')
        login_resp = json.loads(res.json())
        session_cookie = login_resp['cookie']
        login_resp.pop('cookie', None)
        user = login_resp
        user_obj.update(user)
        response = templates.TemplateResponse('index.html', user_obj)
        response.set_cookie(key=session_cookie.key, value=session_cookie.value, httponly=True,secure=True)
    elif res.status_code == 404:
        print(f'404 resp: {res.content}')
        print(f'404 resp json: {res.json()}')
        user_obj.update(res.json())
        response = templates.TemplateResponse('login.html', user_obj)
        response.status_code = 404
    return response

@app.get('/pricing')
async def get_pricing(request: Request):
    return templates.TemplateResponse('pricing.html', {'request': request})

@app.get('/base.html')
async def get_base(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})

@app.get('/contact')
async def get_contact(request: Request):
    return templates.TemplateResponse('contact.html', {'request': request})

@app.get('/legal')
async def get_legal_page(request: Request):
    return templates.TemplateResponse('legal-page.html', {'request': request})

@app.get('/faq')
async def get_faq(request: Request):
    return templates.TemplateResponse('faq.html', {'request': request})

@app.get('/about')
async def get_about(request: Request):
    return templates.TemplateResponse('about.html', {'request': request})
