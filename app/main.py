from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_db_and_tables
from routers.news import router as news_router


app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
