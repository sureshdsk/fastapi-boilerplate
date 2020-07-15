import databases
from fastapi import FastAPI
from app.config import Config

database = databases.Database(Config.DATABASE_URL)

# metadata = sqlalchemy.MetaData()
#
# notes = sqlalchemy.Table(
#     "notes",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("text", sqlalchemy.String),
#     sqlalchemy.Column("completed", sqlalchemy.Boolean),
# )
#
# engine = sqlalchemy.create_engine(
#     Config.DATABASE_URL, connect_args={"check_same_thread": False}
# )
# metadata.create_all(engine)

app = FastAPI(docs_url=Config.DOC_URL, redoc_url=Config.REDOC_URL)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def read_root():
    return {"app": "fastapi-starter-kit"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/test_sql")
async def test_run_sql():
    query = "select now()"
    result = await database.execute(query)
    return {"time_now": result}


@app.get("/tasks")
async def get_tasks_from_db():
    query = "select id, task from test.task limit 10"
    result = await database.fetch_all(query)
    return {"tasks": result}