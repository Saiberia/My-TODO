from fastapi import FastAPI
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='todo/templates')

from todo.routes import home

