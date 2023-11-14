from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount(path='/myapp/static', app=StaticFiles(directory='myapp/static'), name='static')
templates = Jinja2Templates(directory='myapp/templates')


@app.get('/', response_class=HTMLResponse)
# async def index(name: str, request: Request):
async def read_root(name: str, request: Request):
    context = {
        "name": name,
        "request": request
    }
    return templates.TemplateResponse("index.html", context)
# def read_root(name: str):
#     context = {'name': name}
#     return templates.TemplateResponse('index.html', context)


# @app.get('/items/{item_id}')
# def read_item(item_id: int, q: str = None):
#     return {'item_id': item_id, 'q': q}