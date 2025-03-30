from app.database import create_db_and_tables
from app.routers.news import router as news_router
from app.routers.page import router as page_router
from alembic.config import Config
from alembic import command
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    run_alembic_upgrade()
    yield


def run_alembic_upgrade():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


app.include_router(news_router, prefix="/api/news")
app.include_router(page_router)
