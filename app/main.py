from app.database import create_db_and_tables
from app.routers.news import router as news_router
from app.routers.page import router as page_router
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app.include_router(news_router, prefix="/api/news")
app.include_router(page_router)
