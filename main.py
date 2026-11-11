from authx import AuthXConfig, AuthX, TokenPayload

import uvicorn
from fastapi import FastAPI, Form, Depends, Request, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy import select
from starlette import status
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from DataBase import Product, Session

templates = Jinja2Templates(directory='templates')
app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/catalog')
def catalog_page(request: Request):
    with Session() as session:
        products = session.query(Product).all()
    return templates.TemplateResponse(request, 'catalog.html', {'products': products})

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)