import pytest
import requests
import jwt


class TestEndpointReservas:
    BASE_URL = "http://localhost:80/reservas"

    @pytest.mark.integration
    def test_create_nova_reserva_header_faltante(self):
        payload = {
            "id_sessao": "1234-5678-90",
            "id_setor": "1234-5678-90"
        }
        response = requests.post(self.BASE_URL, json=payload)
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data
        assert isinstance(data["detail"], list)
        assert data["detail"][0]["campo"] == "Authorization"
        assert data["detail"][0]["mensagem"] == "Header não informado"

    @pytest.mark.integration
    def test_create_nova_reserva_token_invalido(self):
        headers = {
            "authorization": "Bearer token"
        }
        response = requests.post(self.BASE_URL, headers=headers)
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data
        assert isinstance(data["detail"], list)
        assert data["detail"][0]["campo"] == "Authorization"
        assert data["detail"][0]["mensagem"] == "Token inválido: Not enough segments"

    @pytest.mark.integration
    def test_create_nova_reserva_token_sem_id_cliente(self):
        headers = {
            "authorization": "Bearer " + str(jwt.encode({"id_errado": "1234"}, key="1234"))
        }
        response = requests.post(self.BASE_URL, headers=headers)
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data
        assert isinstance(data["detail"], list)
        assert data["detail"][0]["campo"] == "Authorization"
        assert data["detail"][0]["mensagem"] == 'Token não contém id_cliente'

    @pytest.mark.integration
    def test_create_nova_reserva_payload_faltante(self):
        headers = {
            "authorization": "Bearer " + str(jwt.encode({"id_cliente": "1234"}, key="1234"))
        }
        response = requests.post(self.BASE_URL, headers=headers)
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data
        assert isinstance(data["detail"], list)
        assert data["detail"][0]["campo"] == "id_sessao"
        assert data["detail"][1]["campo"] == "id_setor"

    @pytest.mark.integration
    def test_create_nova_reserva_payload_invalido(self):
        headers = {
            "authorization": "Bearer " + str(jwt.encode({"id_cliente": "1234"}, key="1234"))
        }
        payload = {

        }
        response = requests.post(self.BASE_URL, json=payload, headers=headers)
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data
        assert isinstance(data["detail"], list)
        assert data["detail"][0]["campo"] == "id_sessao"
        assert data["detail"][0]["mensagem"] == "Field required"

    @pytest.mark.integration
    def test_create_nova_reserva_payload_incompleto(self):
        headers = {
            "authorization": "Bearer " + str(jwt.encode({"id_cliente": "1234"}, key="1234"))
        }
        payload = {
            "id_sessao": "1234-5678-90",
            "id_setor": "1234-5678-90"
        }
        response = requests.post(self.BASE_URL, json=payload, headers=headers)
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data
        assert isinstance(data["detail"], list)
        assert data["detail"][0]["campo"] == "id_sessao"
        assert data["detail"][0]["mensagem"] == "String should have at least 36 characters"

    @pytest.mark.integration
    def test_create_nova_reserva_payload_dados_nao_encontrados(self):
        headers = {
            "authorization": "Bearer " + str(jwt.encode({"id_cliente": "1234"}, key="1234"))
        }
        payload = {
            "id_sessao": "c01c1b8a-7fcd-470d-9eef-665cc0e3f979",
            "id_setor": "c01c1b8a-7fcd-470d-9eef-665cc0e3f979"
        }
        response = requests.post(self.BASE_URL, json=payload, headers=headers)
        data = response.json()
        assert "error" in data
        assert data["error"] == "O setor selecionado não existe"

    @pytest.mark.integration
    def test_create_nova_reserva_payload_dados_sucesso(self):
        headers = {
            "authorization": "Bearer " + str(jwt.encode({"id_cliente": "1234"}, key="1234"))
        }
        payload = {
            "id_sessao": "00000000-0000-0000-0000-000000000000",
            "id_setor": "00000000-0000-0000-0000-000000000000"
        }
        response = requests.post(self.BASE_URL, json=payload, headers=headers)
        data = response.json()
        assert "Reserva criada" in data["message"]
