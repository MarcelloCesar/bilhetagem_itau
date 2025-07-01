import pytest
from service_bilhetagem.src.adapters.sqlalchemy_entities.setor import Setor


class TestSetorSQLAlchemyEntity:
    @pytest.mark.unit
    def test_setor_sqlalchemy_entity_repr(self):
        setor = Setor(
            id="setor-1",
            nome="Setor A",
            capacidade=100,
            valor=50.0,
            possui_lugar_marcado=True
        )
        expected_repr = (
            "<Setor(id=setor-1, nome=Setor A, possui_lugar=True)>"
        )
        assert repr(setor) == expected_repr

    @pytest.mark.unit
    def test_setor_sqlalchemy_entity_to_entity(self):
        setor = Setor(
            id="setor-1",
            nome="Setor A",
            capacidade=100,
            valor=50.0,
            possui_lugar_marcado=True
        )
        entity = setor.to_entity()
        assert entity.id == "setor-1"
        assert entity.nome == "Setor A"
        assert entity.capacidade == 100
        assert entity.valor == 50.0
        assert entity.possui_lugar_marcado is True
