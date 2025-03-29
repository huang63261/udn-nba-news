from app.database import engine
from sqlmodel import Session
from typing import Generator


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
