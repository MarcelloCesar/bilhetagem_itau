import pytest
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError
from service_bilhetagem.src.adapters.setor_adapter_sql_alchemy import (
    SetorAdapterSQLAlchemy
)


class TestSetorAdapterSQLAlchemy:
    @pytest.fixture
    def adapter(self):
        self.database_service = MagicMock()
        return SetorAdapterSQLAlchemy(self.database_service)

    @pytest.mark.unit
    def test_get_setor_por_id(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.query.return_value.filter_by.return_value.first.return_value = MagicMock(
            to_entity=lambda: {"id": "setor-1", "nome": "Setor Teste"}
        )
        setor = adapter.get_setor_por_id("setor-1")
        assert setor is not None
        assert setor["id"] == "setor-1"
        assert setor["nome"] == "Setor Teste"

    @pytest.mark.unit
    def test_get_setor_por_id_not_found(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.query.return_value.filter_by.return_value.first.return_value = None
        setor = adapter.get_setor_por_id("setor-1")
        assert setor is None

    @pytest.mark.unit
    def test_get_setor_por_id_exception(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.query.side_effect = SQLAlchemyError("Database error")
        with pytest.raises(Exception):
            adapter.get_setor_por_id("setor-1")
