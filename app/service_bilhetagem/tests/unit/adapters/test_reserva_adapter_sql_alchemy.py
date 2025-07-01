import pytest
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError
from service_bilhetagem.src.adapters.reserva_adapter_sql_alchemy import (
    ReservaAdapterSQLAlchemy
)


class TestReservaAdapterSQLAlchemy:
    @pytest.fixture
    def adapter(self):
        self.database_service = MagicMock()
        return ReservaAdapterSQLAlchemy(self.database_service)

    @pytest.mark.unit
    def test_create_nova_reserva(self, adapter):
        reserva_entity = MagicMock(
            id_ingresso="1234-456",
            id_cliente="cliente-1",
            valor=100.0,
            data_hora_reserva="2023-10-01T10:00:00",
            data_hora_expiracao="2023-10-01T12:00:00",
            situacao="Pendente"
        )
        session_mock = MagicMock()
        session_mock.add.return_value = None
        session_mock.commit.return_value = None
        session_mock.refresh.return_value = None

        adapter.database.get_session = MagicMock(return_value=session_mock)

        result = adapter.create_nova_reserva(reserva_entity)
        assert result.id_ingresso == "1234-456"
        assert result.id_cliente == "cliente-1"
        assert result.valor == 100.0
        assert result.data_hora_reserva == "2023-10-01T10:00:00"
        assert result.data_hora_expiracao == "2023-10-01T12:00:00"
        assert result.situacao == "Pendente"

    @pytest.mark.unit
    def test_create_nova_reserva_exception(self, adapter):
        reserva_entity = MagicMock(
            id_ingresso="1234-456",
            id_cliente="cliente-1",
            valor=100.0,
            data_hora_reserva="2023-10-01T10:00:00",
            data_hora_expiracao="2023-10-01T12:00:00",
            situacao="Pendente"
        )

        adapter.database.get_session = MagicMock(side_effect=SQLAlchemyError("Database error"))

        with pytest.raises(SQLAlchemyError):
            adapter.create_nova_reserva(reserva_entity)
