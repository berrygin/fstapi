from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root():
    content = {"Hello": "World"}
    return templates.TemplateResponse("index.html", context)


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}