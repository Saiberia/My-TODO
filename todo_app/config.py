import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_name = 'Мой менеджер задач'
    db_sqlite_url = 'sqlite:///.\\todo_app\\database\\DB\\todo.db'


settings = Settings()
