import pytest
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError
from service_bilhetagem.src.adapters.ingresso_adapter_sql_alchemy import (
    IngressoAdapterSQLAlchemy
)


class TestIngressoAdapterSQLAlchemy:
    @pytest.fixture
    def adapter(self):
        self.database_service = MagicMock()
        return IngressoAdapterSQLAlchemy(self.database_service)

    @pytest.mark.unit
    def test_get_ingresso_por_id(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.query.return_value.filter_by.return_value.first.return_value = MagicMock(
            to_entity=lambda: {"id": "1234-456", "sessao": "Sessão Teste"}
        )
        ingresso = adapter.get_ingresso_por_id("1234-456")
        assert ingresso is not None
        assert ingresso["id"] == "1234-456"
        assert ingresso["sessao"] == "Sessão Teste"

    @pytest.mark.unit
    def test_get_ingresso_por_id_not_found(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.query.return_value.filter_by.return_value.first.return_value = None
        ingresso = adapter.get_ingresso_por_id("1234-456")
        assert ingresso is None

    @pytest.mark.unit
    def test_get_ingresso_por_id_exception(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.query.side_effect = SQLAlchemyError("Database error")
        with pytest.raises(Exception):
            adapter.get_ingresso_por_id("1234-456")

    @pytest.mark.unit
    def test_get_ingresso_disponivel_para_sessao_e_setor(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.execute.return_value.first.return_value.__getitem__.return_value = MagicMock(
            to_entity=lambda: {"id": "1234-456", "sessao": "Sessão Teste", "setor": "Setor Teste"}
        )
        ingresso = adapter.get_ingresso_disponivel_para_sessao_e_setor("sessao-1", "setor-1")
        assert ingresso is not None
        assert ingresso["id"] == "1234-456"
        assert ingresso["sessao"] == "Sessão Teste"
        assert ingresso["setor"] == "Setor Teste"

    @pytest.mark.unit
    def test_get_ingresso_disponivel_para_sessao_e_setor_not_found(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.execute.return_value.first.return_value = None
        ingresso = adapter.get_ingresso_disponivel_para_sessao_e_setor("sessao-1", "setor-1")
        assert ingresso is None

    @pytest.mark.unit
    def test_get_ingresso_disponivel_para_sessao_e_setor_exception(self,
            adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.execute.side_effect = SQLAlchemyError("Database error")
        with pytest.raises(Exception):
            adapter.get_ingresso_disponivel_para_sessao_e_setor("sessao-1", "setor-1")
