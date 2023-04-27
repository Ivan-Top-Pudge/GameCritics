"""добавили ранк пользователю

Revision ID: ef9e18d2404c
Revises: aaf78964e864
Create Date: 2023-04-09 18:12:00.373035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef9e18d2404c'
down_revision = 'aaf78964e864'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('rank', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'rank')
    op.drop_constraint(None, 'games', type_='unique')
    # ### end Alembic commands ###
