from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import panel as pn
from bokeh.embed import server_document

from myapp.sliders.pn_app import createApp

app = FastAPI()
app.mount(path='/myapp/static', app=StaticFiles(directory='myapp/static'), name='static')
templates = Jinja2Templates(directory='myapp/templates')


# @app.get('/', response_class=HTMLResponse)
# async def index(request: Request):
#     context = {'request': request}
#     return templates.TemplateResponse('index.html', context)

@app.get("/")
async def bkapp_page(request: Request):
    script = server_document('http://127.0.0.1:5000/app')
    return templates.TemplateResponse("base.html", {"request": request, "script": script})

pn.serve({'/app': createApp},
        port=5000, allow_websocket_origin=["127.0.0.1:8000"],
        address="127.0.0.1", show=False)

# async def read_root(name: str, request: Request):
#     context = {
#         "name": name,
#         "request": request
#     }
#     return templates.TemplateResponse("index.html", context)


# @app.get('/items/{item_id}')
# def read_item(item_id: int, q: str = None):
#     return {'item_id': item_id, 'q': q}