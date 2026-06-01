from fastapi import FastAPI

from app.core.config import API_TITLE, API_VERSION
from app.db.session import init_db
from app.fastapi.router import api_router

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    description="API base em FastAPI com SQLite",
)


@app.on_event("startup")
def on_startup() -> None:
    init_db()

app.include_router(api_router)
