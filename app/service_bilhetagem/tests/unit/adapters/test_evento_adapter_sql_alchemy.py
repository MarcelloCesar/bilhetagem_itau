import pytest
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError
from service_bilhetagem.src.adapters.evento_adapter_sql_alchemy import (
    EventoAdapterSQLAlchemy
)


class TestEventoAdapterSQLAlchemy:
    @pytest.fixture
    def adapter(self):
        self.database_service = MagicMock()
        return EventoAdapterSQLAlchemy(self.database_service)

    @pytest.mark.unit
    def test_get_dados_evento_por_id(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.query.return_value.filter_by.return_value.first.return_value = MagicMock(
            to_entity=lambda: {"id": "1234-456", "nome": "Evento Teste"}
        )
        evento = adapter.get_dados_evento_por_id("1234-456")
        assert evento is not None
        assert evento["id"] == "1234-456"
        assert evento["nome"] == "Evento Teste"

    @pytest.mark.unit
    def test_get_dados_evento_por_id_not_found(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.query.return_value.filter_by.return_value.first.return_value = None
        evento = adapter.get_dados_evento_por_id("1234-456")
        assert evento is None

    @pytest.mark.unit
    def test_get_dados_evento_por_id_exception(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.query.side_effect = SQLAlchemyError("Database error")
        with pytest.raises(Exception):
            adapter.get_dados_evento_por_id("1234-456")

    @pytest.mark.unit
    def test_get_lista_eventos(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.query.return_value.all.return_value = [
            MagicMock(to_entity=lambda: {"id": "1234-456", "nome": "Evento Teste 1"}),
            MagicMock(to_entity=lambda: {"id": "7890-123", "nome": "Evento Teste 2"})
        ]
        eventos = adapter.get_lista_eventos()
        assert len(eventos) == 2
        assert eventos[0]["id"] == "1234-456"
        assert eventos[0]["nome"] == "Evento Teste 1"
        assert eventos[1]["id"] == "7890-123"
        assert eventos[1]["nome"] == "Evento Teste 2"

    @pytest.mark.unit
    def test_get_lista_eventos_empty(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.query.return_value.all.return_value = []
        eventos = adapter.get_lista_eventos()
        assert eventos == []

    @pytest.mark.unit
    def test_get_lista_eventos_exception(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.query.side_effect = SQLAlchemyError("Database error")
        with pytest.raises(Exception):
            adapter.get_lista_eventos()
