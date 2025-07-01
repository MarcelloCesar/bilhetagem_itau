import pytest
from service_bilhetagem.src.adapters.sqlalchemy_entities.sessao import Sessao


class TestSessaoSQLAlchemyEntity:
    @pytest.mark.unit
    def test_sessao_sqlalchemy_entity_repr(self):
        sessao = Sessao(
            id="sessao-1",
            id_evento="evento-1",
            data="2023-10-01",
            horario_inicio="19:00:00"
        )
        expected_repr = (
            "<Sessao(id=sessao-1, "
            "data=2023-10-01, horario_inicio=19:00:00)>"
        )
        assert repr(sessao) == expected_repr

    @pytest.mark.unit
    def test_sessao_sqlalchemy_entity_to_entity(self):
        sessao = Sessao(
            id="sessao-1",
            data="2023-10-01",
            horario_inicio="19:00:00"
        )
        entity = sessao.to_entity()
        assert entity.id == "sessao-1"
        assert entity.data == "2023-10-01"
        assert entity.horario_inicio == "19:00:00"
