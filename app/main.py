from fastapi import FastAPI, Depends
from config import Config
from sqlalchemy.orm import Session
from database import get_db

app = FastAPI(docs_url=Config.DOC_URL, redoc_url=Config.REDOC_URL)


@app.get("/")
def read_root():
    return {"app": "fastapi-starter-kit"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/test_sql")
def test_run_sql(db: Session = Depends(get_db)):
    query = "select now()"
    query_exec = db.execute(query)
    rs = query_exec.fetchone()
    return {"time_now": rs[0]}


@app.get("/tasks")
def get_tasks_from_db(db: Session = Depends(get_db)):
    query = "select id, task from test.task limit 10"
    query_exec = db.execute(query)
    result = [dict(task) for task in query_exec]
    return {"tasks": result}