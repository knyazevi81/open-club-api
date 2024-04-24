
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
from .routes import home

app = FastAPI()

app.mount("/static", StaticFiles(directory="routes/templates/static"), name="static")

app.include_router(home.route)

#if __name__ == '__main__':
#    print(f"API running {HOST}:{PORT}")
#    uvicorn.run(app, host=HOST, port=PORT)



