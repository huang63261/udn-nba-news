"""add index on url

Revision ID: f718c5b7c860
Revises: a3d2d482099c
Create Date: 2025-03-30 18:47:52.158113

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f718c5b7c860"
down_revision: Union[str, None] = "a3d2d482099c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index("ix_news_url", "news", ["url"])


def downgrade() -> None:
    op.drop_index("ix_news_url", "news")
