from unittest.mock import MagicMock
import pytest
from service_bilhetagem.src.usecases.sessao_usecase import SessaoUseCase


class TestSessaoUseCase:
    def setup_method(self):
        self.mock_repository = MagicMock()
        self.use_case = SessaoUseCase(sessao_repository=self.mock_repository)

    @pytest.mark.unit
    def test_get_dados_sessoes_ativas_para_o_evento_success(self):
        self.mock_repository.get_dados_sessoes_ativas_para_o_evento.return_value = [
            MagicMock(id_sessao="1", data_sessao="2023-10-01",
                      horario_inicio="12:00", setor_id="1",
                      setor_nome="Setor A", possui_lugar_marcado=True,
                      ingressos_disponiveis=100, cadeiras_disponiveis=50)
        ]
        response = self.use_case.get_dados_sessoes_ativas_para_o_evento("1")
        assert response == {
            "sessoes": [{
                "id_sessao": "1",
                "data_sessao": "2023-10-01",
                "horario_inicio": "12:00",
                "setor": {"id": "1", "nome": "Setor A"},
                "possui_lugar_marcado": True,
                "ingressos_disponiveis": 100,
                "cadeiras_disponiveis": 50
            }]
        }

    @pytest.mark.unit
    def test_get_dados_sessoes_ativas_para_o_evento_not_found(self):
        self.mock_repository.get_dados_sessoes_ativas_para_o_evento.return_value = []
        response = self.use_case.get_dados_sessoes_ativas_para_o_evento("999")
        assert response == {"error": "Nenhuma sessão ativa encontrada para o evento"}