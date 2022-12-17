"""empty message

Revision ID: 352e281c52f6
Revises: e75cdefe8865
Create Date: 2022-12-12 00:41:51.557977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '352e281c52f6'
down_revision = 'e75cdefe8865'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.alter_column('seeking_talent',
               existing_type=sa.INTEGER(),
               type_=sa.Boolean(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.alter_column('seeking_talent',
               existing_type=sa.Boolean(),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
