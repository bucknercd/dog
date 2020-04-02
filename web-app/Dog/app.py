from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/')
async def get_index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/login')
async def get_login_page(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})

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
