from app.crud import news as news_crud
from app.dependency import get_session
from app.services.crawler import fetch_feature_news
from app.models import News
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

router = APIRouter()


@router.get("/crawl-news/")
def crawl_and_save_news(session: Session = Depends(get_session)):
    news_data = fetch_feature_news()

    existing_urls = {row for row in session.exec(select(News.url)).all()}

    new_items = [news for news in news_data if news["url"] not in existing_urls]

    news_models = [News(**data) for data in new_items]

    news_crud.create_news_batch(session, news_models)

    return {"inserted": len(news_models)}


@router.get("/")
def get_all_news(session: Session = Depends(get_session)):
    news = news_crud.get_all_news(session)
    return news


@router.get("/{id}", response_model=News)
def get_news(id: int, session: Session = Depends(get_session)):
    news = session.get(News, id)

    if not news:
        raise HTTPException(status_code=404, detail="News doesn't exist")

    return news


@router.post("/", response_model=News)
def create_news(news: News, session: Session = Depends(get_session)):
    statement = select(News).where(News.url == news.url)
    existing = session.exec(statement).first()
    if existing:
        raise HTTPException(status_code=400, detail="News with this URL already exists")

    created_news = news_crud.create_news(session, news)
    return created_news


@router.get("/ping-db")
def ping_db(session: Session = Depends(get_session)):
    result = session.exec(select(News)).all()
    return {"status": "ok", "row_count": len(result)}
