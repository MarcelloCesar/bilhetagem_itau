from sqlalchemy import Column, String, ForeignKey, Date, Time
from ...domain.entities.sessao_entity import SessaoEntity
from .base import Base
from uuid import uuid4


class Sessao(Base):
    __tablename__ = 'sessao'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    id_evento = Column(String(36), ForeignKey('evento.id'), nullable=False)
    data = Column(Date, nullable=False)
    horario_inicio = Column(Time, nullable=False)

    def __repr__(self):
        return f"<Sessao(id={self.id}, data={self.data}, horario_inicio={self.horario_inicio})>"

    def to_entity(self):
        return SessaoEntity(
            id=self.id,
            data=self.data,
            id_evento=self.id_evento,
            horario_inicio=self.horario_inicio,
        )
