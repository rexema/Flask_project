"""empty message

Revision ID: 52f6c42d0e33
Revises: f5c5bd0be89b
Create Date: 2023-05-05 12:09:58.763438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52f6c42d0e33'
down_revision = 'f5c5bd0be89b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nick', sa.String(length=255), server_default='', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('nick')

    # ### end Alembic commands ###
