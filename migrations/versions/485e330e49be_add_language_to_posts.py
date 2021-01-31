"""add language to posts

Revision ID: 485e330e49be
Revises: 2f25c0ac9e14
Create Date: 2021-01-31 16:28:43.070553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '485e330e49be'
down_revision = '2f25c0ac9e14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###