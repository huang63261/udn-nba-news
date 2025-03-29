from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import create_db_and_tables
from routers.news import router as news_router
from routers.page import router as page_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app.include_router(news_router, prefix="/api/news")
app.include_router(page_router, prefix="/news")
