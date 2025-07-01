import pytest
from service_bilhetagem.src.adapters.sqlalchemy_entities.evento import (
    Evento
)


class TestEventoSQLAlchemyEntity:
    @pytest.mark.unit
    def test_evento_sqlalchemy_entity_repr(self):
        evento = Evento(
            id="1234-456",
            nome="Evento Teste")
        expected_repr = \
            "<Evento(id=1234-456, nome=Evento Teste)>"
        assert repr(evento) == expected_repr

    @pytest.mark.unit
    def test_evento_sqlalchemy_entity_to_entity(self):
        evento = Evento(
            id="1234-456",
            nome="Evento Teste")
        entity = evento.to_entity()
        assert entity.id == "1234-456"
        assert entity.nome == "Evento Teste"
