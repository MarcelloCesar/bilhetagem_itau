import pytest
import requests


class TestEndpointEventos:
    BASE_URL = "http://localhost:80/eventos"

    @pytest.mark.integration
    def test_get_dados_evento_por_id(self):
        response = requests.get(f"{self.BASE_URL}/1234-5678-90")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == "1234-5678-90"
        assert data["nome"] == "Mock"

    @pytest.mark.integration
    def test_get_dados_evento_por_id_not_found(self):
        response = requests.get(f"{self.BASE_URL}/not-found-id")
        data = response.json()
        assert data["error"] == "Evento não encontrado"

    @pytest.mark.integration
    def test_get_dados_evento_por_id_invalid_id_rota_invalida(self):
        response = requests.get(f"{self.BASE_URL}/1234-5678-90/testeteste")
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Not Found"

    @pytest.mark.integration
    def test_get_lista_eventos(self):
        response = requests.get(self.BASE_URL)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

    @pytest.mark.integration
    def test_get_lista_eventos_endpoint_invalido(self):
        response = requests.get(self.BASE_URL + "ssss")
        assert response.status_code == 404
        data = response.json()
        assert data["detail"] == "Not Found"
