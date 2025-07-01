import pytest
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError
from service_bilhetagem.src.adapters.sessao_adapter_sql_alchemy import (

    SessaoAdapterSQLAlchemy
)


class TestSessaoAdapterSQLAlchemy:
    @pytest.fixture
    def adapter(self):
        self.database_service = MagicMock()
        return SessaoAdapterSQLAlchemy(self.database_service)

    @pytest.mark.unit
    def test_get_dados_sessoes_ativas_para_o_evento(self, adapter):
        adapter.database.get_session = MagicMock()
        adapter.database.get_session.return_value.execute.return_value.all.return_value = [
            MagicMock(
                __getitem__=lambda x, y: "mocked_value" if y == 0 else None
            )
        ]
        result = adapter.get_dados_sessoes_ativas_para_o_evento("evento-1")
        assert len(result) == 1
        assert result[0].id_sessao == "mocked_value"

    @pytest.mark.unit
    def test_get_dados_sessoes_ativas_para_o_evento_exception(self, adapter):
        adapter.database.get_session = MagicMock(side_effect=SQLAlchemyError("Database error"))
        with pytest.raises(SQLAlchemyError):
            adapter.get_dados_sessoes_ativas_para_o_evento("evento-1")