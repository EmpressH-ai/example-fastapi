"""add content to posts table

Revision ID: dbc4c19ad87c
Revises: 5d42bf9db570
Create Date: 2023-10-26 13:06:00.083587

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "dbc4c19ad87c"
down_revision: Union[str, None] = "5d42bf9db570"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
