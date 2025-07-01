import pytest
import requests


class TestEndpointSessao:
    BASE_URL = "http://localhost:80/eventos/1234-5678-90/sessoes"

    @pytest.mark.integration
    def test_get_sessoes_disponiveis_evento(self):
        response = requests.get(self.BASE_URL)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) > 0

    @pytest.mark.integration
    def test_get_sessoes_disponiveis_evento_not_found(self):
        response = requests.get(self.BASE_URL.replace("1234-5678-90", "not-found-id"))
        data = response.json()
        assert data["error"] == "Nenhuma sessão ativa encontrada para o evento"

    @pytest.mark.integration
    def test_get_sessoes_disponiveis_evento_url_invalida(self):
        response = requests.get(self.BASE_URL + "test")
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Not Found"
