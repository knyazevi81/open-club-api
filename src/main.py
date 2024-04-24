
"""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from routes.home import route as main_menue

app = FastAPI()

app.mount('/static', StaticFiles(directory="routes/templates/static"), name="static")

app.include_router(main_menue)

"""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles

from pathlib import Path
import sys
sys.path.append(str(Path(Path().resolve, "/routes")))

from routes.home import route as main_menue
import os



import uvicorn

HOST = "0.0.0.0"
PORT = int("8000")
USE_NGROK = True 

app = FastAPI()

if USE_NGROK:
    from pyngrok import ngrok

    # https://dashboard.ngrok.com/get-started/your-authtoken
    ngrok.set_auth_token("a") 

    public_url = ngrok.connect(PORT).public_url
    print(f"ngrok tunnel {public_url}/home")

app.mount("/static", StaticFiles(directory="routes/templates/static"), name="static")

app.include_router(main_menue)

#if __name__ == '__main__':
#    print(f"API running {HOST}:{PORT}")
#    uvicorn.run(app, host=HOST, port=PORT)


