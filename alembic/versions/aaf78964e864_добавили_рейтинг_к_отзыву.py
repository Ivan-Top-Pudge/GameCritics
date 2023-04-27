"""добавили рейтинг к отзыву

Revision ID: aaf78964e864
Revises: 
Create Date: 2023-04-09 16:57:49.831732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aaf78964e864'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('rate', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reviews', 'rate')
    # ### end Alembic commands ###
