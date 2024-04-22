from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pathlib import Path

route = APIRouter(tags=['home'])
BASE_DIR = Path(__file__).resolve()
templates = Jinja2Templates(directory=str(Path(BASE_DIR, "templates")))

@route.get("/home", response_class=HTMLResponse)
def home_tasks(requets: Request):
    return templates.TemplateResponse(
        request=requets, name="home.html"
    )

