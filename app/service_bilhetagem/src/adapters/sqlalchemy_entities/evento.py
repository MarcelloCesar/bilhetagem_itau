from sqlalchemy import Column, String
from ...domain.entities.evento_entity import EventoEntity
from .base import Base
from uuid import uuid4


class Evento(Base):
    __tablename__ = 'evento'

    id = id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)

    def __repr__(self):
        return f"<Evento(id={self.id}, nome={self.nome})>"

    def to_entity(self):
        return EventoEntity(
            id=self.id,
            nome=self.nome
        )
