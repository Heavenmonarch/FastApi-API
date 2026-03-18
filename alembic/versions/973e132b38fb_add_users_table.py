"""add users table

Revision ID: 973e132b38fb
Revises: 56022e0ab645
Create Date: 2026-03-18 14:26:56.795332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '973e132b38fb'
down_revision: Union[str, Sequence[str], None] = '56022e0ab645'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(),nullable=False), sa.Column('email', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False), sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
