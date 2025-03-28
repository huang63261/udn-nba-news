"""create news table

Revision ID: a3d2d482099c
Revises:
Create Date: 2025-03-28 17:16:50.163929

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a3d2d482099c"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "news",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(50), nullable=False),
        sa.Column("url", sa.String(60), nullable=False),
        sa.Column("content", sa.Text()),
        sa.Column("image_url", sa.String(60)),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("news")
