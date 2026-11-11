from authx import AuthXConfig, AuthX, TokenPayload

import uvicorn
from fastapi import FastAPI, Form, Depends, Request, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy import select
from starlette import status
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates