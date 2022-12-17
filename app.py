import os

import uvicorn
from todo.main import app

if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=os.getenv("PORT", default=5000), log_level="info")
