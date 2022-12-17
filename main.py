import os

import uvicorn
from todo.app import app

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=os.getenv("PORT", default=3000), log_level="info")
