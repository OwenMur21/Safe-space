"""Initial Migration

Revision ID: 618c1b2e8baf
Revises: 
Create Date: 2018-09-18 20:32:41.459281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '618c1b2e8baf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('pass_secure', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('username')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('crisis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_name'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_name'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('health',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_name'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mental',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_name'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('crisiscomments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('crisis_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['crisis_id'], ['crisis.id'], ),
    sa.ForeignKeyConstraint(['user_name'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('famcomments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('fam_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['fam_id'], ['fams.id'], ),
    sa.ForeignKeyConstraint(['user_name'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('healthcomments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('health_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['health_id'], ['health.id'], ),
    sa.ForeignKeyConstraint(['user_name'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mentalcomments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('mental_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['mental_id'], ['mental.id'], ),
    sa.ForeignKeyConstraint(['user_name'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mentalcomments')
    op.drop_table('healthcomments')
    op.drop_table('famcomments')
    op.drop_table('crisiscomments')
    op.drop_table('mental')
    op.drop_table('health')
    op.drop_table('fams')
    op.drop_table('crisis')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###