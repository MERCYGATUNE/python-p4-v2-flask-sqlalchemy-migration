"""rename department

Revision ID: 532f6edb5290
Revises: e84719d636e6
Create Date: 2024-07-13 13:33:18.663450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '532f6edb5290'
down_revision = 'e84719d636e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department','departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('address', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.rename_table('departments','department')
    # ### end Alembic commands ###
