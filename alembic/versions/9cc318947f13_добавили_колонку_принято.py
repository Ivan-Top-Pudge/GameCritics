"""добавили колонку принято

Revision ID: 9cc318947f13
Revises: ef9e18d2404c
Create Date: 2023-04-16 20:31:31.786690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cc318947f13'
down_revision = 'ef9e18d2404c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('approved', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'approved')
    op.drop_constraint(None, 'games', type_='unique')
    op.drop_column('games', 'approved')
    # ### end Alembic commands ###
