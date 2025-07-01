from unittest.mock import MagicMock
import pytest
from service_bilhetagem.src.usecases.reserva_usecase import ReservaUseCase


class TestReservaUseCase:
    def setup_method(self):
        self.mock_reserva_repo = MagicMock()
        self.mock_setor_repo = MagicMock()
        self.mock_ingresso_repo = MagicMock()
        self.use_case = ReservaUseCase(
            reserva_repository=self.mock_reserva_repo,
            setor_repository=self.mock_setor_repo,
            ingresso_repository=self.mock_ingresso_repo
        )

    @pytest.mark.unit
    def test_create_nova_reserva_success(self):
        request = MagicMock(id_setor="1", id_sessao="1", cadeira="A1")
        self.mock_setor_repo.get_setor_por_id.return_value = MagicMock(
            possui_lugar_marcado=True)
        self.mock_ingresso_repo.get_ingresso_disponivel_para_sessao_e_setor.return_value = MagicMock(
            id="ingresso1", id_sessao="1", id_setor="1", cadeira="A1")
        self.mock_reserva_repo.create_nova_reserva.return_value = MagicMock(
            id="reserva1", id_ingresso="ingresso1", id_sessao="1")
        response = self.use_case.create_nova_reserva(request)
        assert response == {"message": "Reserva criada: " + "reserva1"}

    @pytest.mark.unit
    def test_create_nova_reserva_setor_not_found(self):
        request = MagicMock(id_setor="999")
        self.mock_setor_repo.get_setor_por_id.return_value = None

        response = self.use_case.create_nova_reserva(request)
        assert response == {"error": "O setor selecionado não existe"}

    @pytest.mark.unit
    def test_create_nova_reserva_cadeira_required(self):
        request = MagicMock(id_setor="1", possui_lugar_marcado=True, cadeira=None)
        self.mock_setor_repo.get_setor_por_id.return_value = MagicMock(
            possui_lugar_marcado=True)

        response = self.use_case.create_nova_reserva(request)
        assert response == {
            "error": "Para setores com lugares marcados, é necessário informar a cadeira"
        }

    @pytest.mark.unit
    def test_create_nova_reserva_cadeira_not_required(self):
        request = MagicMock(id_setor="1", possui_lugar_marcado=False, cadeira="A1")
        self.mock_setor_repo.get_setor_por_id.return_value = MagicMock(
            possui_lugar_marcado=False)

        response = self.use_case.create_nova_reserva(request)
        assert response == {
            "error": "Para setores sem lugares marcados, não é necessário informar a cadeira"
        }

    @pytest.mark.unit
    def test_create_nova_reserva_sem_Tickets_disponiveis(self):
        request = MagicMock(id_setor="1", id_sessao="1", cadeira="A1")
        self.mock_setor_repo.get_setor_por_id.return_value = MagicMock(
            possui_lugar_marcado=True)
        self.mock_ingresso_repo.get_ingresso_disponivel_para_sessao_e_setor.return_value = None

        response = self.use_case.create_nova_reserva(request)
        assert response == {"error": "Não há ingressos disponíveis para os parametros informados"}
