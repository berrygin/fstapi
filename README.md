### 起動

```shell
uvicorn myapp.main:app --reload 
```
o http://127.0.0.1:8000/
x localhost:8000

```
uvicorn myapp.main:app --host 0.0.0.0 --port $PORT
```