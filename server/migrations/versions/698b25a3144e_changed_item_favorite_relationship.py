"""changed item favorite relationship

Revision ID: 698b25a3144e
Revises: 98a5483d97a5
Create Date: 2023-07-18 14:55:16.097804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '698b25a3144e'
down_revision = '98a5483d97a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('item_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'items', ['item_id'], ['id'])

    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('favorite_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favorite_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key(None, 'favorites', ['favorite_id'], ['id'])

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('item_id')

    # ### end Alembic commands ###