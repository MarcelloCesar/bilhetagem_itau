import pytest
from service_bilhetagem.src.adapters.sqlalchemy_entities.reserva import Reserva
from datetime import datetime


class TestReservaSQLAlchemyEntity:
    @pytest.mark.unit
    def test_reserva_sqlalchemy_entity_repr(self):
        reserva = Reserva(
            id="1234-456",
            id_ingresso="1234-456",
            id_cliente="cliente-1",
            valor=100.0,
            data_hora_reserva="2023-10-01T10:00:00",
            data_hora_expiracao="2023-10-01T12:00:00",
            situacao="Pendente"
        )

        expected_repr = (
            "<Reserva(id=1234-456, valor=100.0, situacao=Pendente)>"
        )
        assert repr(reserva) == expected_repr

    @pytest.mark.unit
    def test_reserva_sqlalchemy_entity_to_entity(self):
        reserva = Reserva(
            id_ingresso="1234-456",
            id_cliente="cliente-1",
            valor=100.0,
            data_hora_reserva=datetime.strptime("2023-10-01T10:00:00", "%Y-%m-%dT%H:%M:%S"),
            data_hora_expiracao=datetime.strptime("2023-10-01T12:00:00", "%Y-%m-%dT%H:%M:%S"),
            situacao="ANALISE"
        )
        entity = reserva.to_entity()
        assert entity.id_ingresso == "1234-456"
        assert entity.id_cliente == "cliente-1"
        assert entity.valor == 100.0
        assert entity.situacao == "ANALISE"

    @pytest.mark.unit
    def test_reserva_sqlalchemy_entity_to_entity_situacao_invalida(self):
        reserva = Reserva(
            id_ingresso="1234-456",
            id_cliente="cliente-1",
            valor=100.0,
            data_hora_reserva=datetime.strptime("2023-10-01T10:00:00", "%Y-%m-%dT%H:%M:%S"),
            data_hora_expiracao=datetime.strptime("2023-10-01T12:00:00", "%Y-%m-%dT%H:%M:%S"),
            situacao="Invalida"
        )
        with pytest.raises(ValueError, match="situacao deve ser 'ANALISE' ou 'CONFIRMADA'"):
            reserva.to_entity()

    @pytest.mark.unit
    def test_reserva_sqlalchemy_entity_to_entity_data_inicio_invalida(self):
        reserva = Reserva(
            id_ingresso="1234-456",
            id_cliente="cliente-1",
            valor=100.0,
            data_hora_reserva=3,
            data_hora_expiracao=datetime.strptime("2023-10-01T10:00:00", "%Y-%m-%dT%H:%M:%S"),
            situacao="ANALISE"
        )
        with pytest.raises(TypeError, match="data_hora_reserva deve ser do tipo datetime"):
            reserva.to_entity()

    @pytest.mark.unit
    def test_reserva_sqlalchemy_entity_to_entity_data_fim_invalida(self):
        reserva = Reserva(
            id_ingresso="1234-456",
            id_cliente="cliente-1",
            valor=100.0,
            data_hora_reserva=datetime.strptime("2023-10-01T10:00:00", "%Y-%m-%dT%H:%M:%S"),
            data_hora_expiracao=3,
            situacao="ANALISE"
        )
        with pytest.raises(TypeError, match="data_hora_expiracao deve ser do tipo datetime"):
            reserva.to_entity()
