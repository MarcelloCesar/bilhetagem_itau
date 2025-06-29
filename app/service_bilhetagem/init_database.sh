#!/bin/bash

# Nome do arquivo do banco SQLite
DB_FILE="service_bilhetagem.db"

# Caminho onde ficará o diretório do Alembic
ALEMBIC_DIR="alembic"

# Remove banco e alembic antigos (cuidado!)
rm -f "$DB_FILE"
rm -rf "$ALEMBIC_DIR"

# Cria banco SQLite vazio
touch "$DB_FILE"

# Inicializa Alembic
alembic init "$ALEMBIC_DIR"

# Atualiza o alembic.ini para usar SQLite (substitui inplace)
sed -i "s|sqlalchemy.url = .*|sqlalchemy.url = sqlite:///./$DB_FILE|" alembic.ini

# Copia model base e configura env.py para usar metadados
# (Ajude Alembic a localizar os modelos)
# Substitui linha que contém "target_metadata = None"
sed -i "s|target_metadata = None|from src.adapters.sqlalchemy_entities.base import Base\nfrom src.adapters.sqlalchemy_entities.evento import Evento\ntarget_metadata = Base.metadata|" "$ALEMBIC_DIR/env.py"


# Gera primeira migration
alembic revision --autogenerate -m "criação de tabelas iniciais"

# Aplica migrations
alembic upgrade head

python popula_database.py

echo "Banco SQLite e Alembic inicializados com sucesso!"
