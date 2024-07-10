"""empty message

Revision ID: b3207a8287e7
Revises: 
Create Date: 2024-07-10 10:50:55.788710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3207a8287e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('tid', sa.Integer(), nullable=False),
    sa.Column('task', sa.String(length=50), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('tid'),
    sa.UniqueConstraint('task')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    # ### end Alembic commands ###
