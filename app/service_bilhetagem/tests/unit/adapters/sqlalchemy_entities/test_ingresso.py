import pytest
from service_bilhetagem.src.adapters.sqlalchemy_entities.ingresso import Ingresso


class TestIngressoSQLAlchemyEntity:
    @pytest.mark.unit
    def test_ingresso_sqlalchemy_entity_repr(self):
        ingresso = Ingresso(
            id="1234-456",
            id_sessao="sessao-1",
            id_setor="setor-1",
            cadeira="A1",
            valor=50.0
        )
        expected_repr = "<Ingresso(id=1234-456, cadeira=A1, valor=50.0)>"
        assert repr(ingresso) == expected_repr

    @pytest.mark.unit
    def test_ingresso_sqlalchemy_entity_to_entity(self):
        ingresso = Ingresso(
            id="1234-456",
            id_sessao="sessao-1",
            id_setor="setor-1",
            cadeira="A1",
            valor=50.0
        )
        entity = ingresso.to_entity()
        assert entity.id == "1234-456"
        assert entity.id_sessao == "sessao-1"
        assert entity.id_setor == "setor-1"
        assert entity.cadeira == "A1"
        assert entity.valor == 50.0
