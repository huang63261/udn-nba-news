from app.models import News
from typing import List
from sqlmodel import Session, select


def create_news(session: Session, news: News) -> News:
    session.add(news)
    session.commit()
    session.refresh(news)
    return news


def create_news_batch(session: Session, news_list: List[News]) -> int:
    session.add_all(news_list)
    session.commit()
    return len(news_list)


def get_all_news(session: Session) -> List[News]:
    return session.exec(select(News)).all()


def get_news_by_id(session: Session, news_id: int) -> News | None:
    return session.get(News, news_id)


def delete_news_by_id(session: Session, news_id: int) -> bool:
    news = session.get(News, news_id)
    if not news:
        return False
    session.delete(news)
    session.commit()
    return True
