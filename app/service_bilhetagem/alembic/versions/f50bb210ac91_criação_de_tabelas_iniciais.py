"""criação de tabelas iniciais

Revision ID: f50bb210ac91
Revises: 
Create Date: 2025-06-30 23:02:37.101367

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f50bb210ac91'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('evento',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('descricao', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('setor',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('capacidade', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.Column('possui_lugar_marcado', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sessao',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('id_evento', sa.String(length=36), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.Column('horario_inicio', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['id_evento'], ['evento.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ingresso',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('id_sessao', sa.String(length=36), nullable=False),
    sa.Column('id_setor', sa.String(length=36), nullable=False),
    sa.Column('cadeira', sa.String(), nullable=True),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['id_sessao'], ['sessao.id'], ),
    sa.ForeignKeyConstraint(['id_setor'], ['setor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reserva',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('id_ingresso', sa.String(length=36), nullable=False),
    sa.Column('id_cliente', sa.String(length=36), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.Column('data_hora_reserva', sa.DateTime(), nullable=False),
    sa.Column('data_hora_expiracao', sa.DateTime(), nullable=False),
    sa.Column('situacao', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_ingresso'], ['ingresso.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reserva')
    op.drop_table('ingresso')
    op.drop_table('sessao')
    op.drop_table('setor')
    op.drop_table('evento')
    # ### end Alembic commands ###
