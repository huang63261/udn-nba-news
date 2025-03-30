import sqlalchemy as sa
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class News(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    url: str = Field(index=True)
    content: Optional[str] = Field(default=None, sa_column=sa.Column(sa.Text()))
    image_url: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now)
