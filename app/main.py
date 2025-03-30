from app.routers.news import router as news_router
from app.routers.page import router as page_router
from alembic.config import Config
from alembic import command
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def run_alembic_upgrade():
    print("🔧 Running Alembic migration")
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


@asynccontextmanager
async def lifespan(app: FastAPI):
    run_alembic_upgrade()
    yield


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(news_router, prefix="/api/news")
app.include_router(page_router)
