"""empty message

Revision ID: 3bfa4c28c75a
Revises: 4ec901e8decc
Create Date: 2017-09-07 00:44:02.488504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bfa4c28c75a'
down_revision = '4ec901e8decc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=True),
    sa.Column('password', sa.String(length=250), nullable=True),
    sa.Column('firstname', sa.String(length=100), nullable=True),
    sa.Column('lastname', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('lists',
    sa.Column('list_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('list_name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'users.user_id'], ),
    sa.PrimaryKeyConstraint('list_id')
    )
    op.create_table('items',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('list_id', sa.Integer(), nullable=True),
    sa.Column('item_name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['list_id'], [u'lists.list_id'], ),
    sa.PrimaryKeyConstraint('item_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('lists')
    op.drop_table('users')
    # ### end Alembic commands ###
