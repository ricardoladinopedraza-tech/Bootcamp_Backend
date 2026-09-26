"""estado inicial

Revision ID: 3965e7b974fd
Revises: 
Create Date: 2026-09-04 05:22:40.113244

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3965e7b974fd'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "usuarios",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(), nullable=True),
        sa.Column("correo", sa.String(), nullable=True),
    )

    op.create_table(
        "pedidos",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("producto", sa.String(), nullable=True),
        sa.Column("usuario_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["usuario_id"],
            ["usuarios.id"]
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_table("pedidos")
    op.drop_table("usuarios")
