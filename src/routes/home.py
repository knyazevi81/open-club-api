from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pathlib import Path

route = APIRouter(tags=['home'])
BASE_DIR = Path(__file__).parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, "templates")))

@route.get("/home", response_class=HTMLResponse)
def home_tasks(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html"
    )


@route.get("/mock")
def mock_task():
    return {
    "data": {
        "clubName": "<p>Parus</p>",
        "clubId": "<p>102-2</p>",
        "ClubPm": "<p>Khasan</p>"
    }
}
