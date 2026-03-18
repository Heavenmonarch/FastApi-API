"""add content column to posts table

Revision ID: 56022e0ab645
Revises: 9c7d60c86788
Create Date: 2026-03-18 14:14:46.891692

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56022e0ab645'
down_revision: Union[str, Sequence[str], None] = '9c7d60c86788'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
