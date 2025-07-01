from unittest.mock import MagicMock
import pytest
from service_bilhetagem.src.usecases.evento_usecase import EventoUseCase


class TestEventoUseCase:
    def setup_method(self):
        self.mock_repository = MagicMock()
        self.use_case = EventoUseCase(evento_repository=self.mock_repository)

    @pytest.mark.unit
    def test_get_dados_evento_success(self):
        self.mock_repository.get_dados_evento_por_id.return_value = MagicMock(
            id="1", nome="Evento Teste", descricao="Descrição do evento"
        )
        response = self.use_case.get_dados_evento("1")
        assert response == {
            "id": "1",
            "nome": "Evento Teste",
            "descricao": "Descrição do evento"
        }

    @pytest.mark.unit
    def test_get_dados_evento_not_found(self):
        self.mock_repository.get_dados_evento_por_id.return_value = None
        response = self.use_case.get_dados_evento("999")
        assert response == {"error": "Evento não encontrado"}

    @pytest.mark.unit
    def test_get_lista_eventos_success(self):
        self.mock_repository.get_lista_eventos.return_value = [
            MagicMock(id="1", nome="Evento 1", descricao="Descrição 1"),
            MagicMock(id="2", nome="Evento 2", descricao=None)
        ]
        response = self.use_case.get_lista_eventos()
        assert response == [
            {"id": "1", "nome": "Evento 1", "descricao": "Descrição 1"},
            {"id": "2", "nome": "Evento 2", "descricao": None}
        ]

    @pytest.mark.unit
    def test_get_lista_eventos_empty(self):
        self.mock_repository.get_lista_eventos.return_value = []
        response = self.use_case.get_lista_eventos()
        assert response == {"error": "Nenhum evento encontrado"}
