"""empty message

Revision ID: b1219bd26630
Revises: eff1c4efac0f
Create Date: 2020-03-29 13:08:06.702314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1219bd26630'
down_revision = 'eff1c4efac0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todos', 'todolists', ['list_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'list_id')
    op.drop_table('todolists')
    # ### end Alembic commands ###
