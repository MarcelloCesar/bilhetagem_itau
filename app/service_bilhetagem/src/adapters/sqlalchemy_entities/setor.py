from sqlalchemy import Column, String, Integer, Float, Boolean
from ...domain.entities.setor_entity import SetorEntity
from .base import Base
from uuid import uuid4


class Setor(Base):
    __tablename__ = 'setor'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    nome = Column(String, nullable=False)
    capacidade = Column(Integer, nullable=False)
    valor = Column(Float, nullable=False)
    possui_lugar_marcado = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<Setor(id={self.id}, nome={self.nome}, possui_lugar={self.possui_lugar_marcado})>"

    def to_entity(self):
        return SetorEntity(
            id=self.id,
            nome=self.nome,
            capacidade=self.capacidade,
            valor=self.valor,
            possui_lugar_marcado=self.possui_lugar_marcado
        )
