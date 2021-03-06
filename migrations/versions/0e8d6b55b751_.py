"""empty message

Revision ID: 0e8d6b55b751
Revises: 61df5399663a
Create Date: 2017-08-16 15:34:51.738525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e8d6b55b751'
down_revision = '61df5399663a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.drop_index('ix_user_nickname', table_name='user')
    op.drop_column('user', 'nickname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('nickname', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.create_index('ix_user_nickname', 'user', ['nickname'], unique=True)
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
