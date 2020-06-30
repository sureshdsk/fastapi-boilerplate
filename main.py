from fastapi import FastAPI
from config import Config

app = FastAPI(docs_url=Config.DOC_URL, redoc_url=Config.REDOC_URL)


@app.get("/")
def read_root():
    return {"app": "fastapi-starter-kit"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}