from fastapi import FastAPI
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='todo_app/templates')

from todo_app.routes import home

