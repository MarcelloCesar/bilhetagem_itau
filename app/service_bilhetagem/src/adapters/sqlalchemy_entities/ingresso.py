from sqlalchemy import Column, String, ForeignKey, Float
from ...domain.entities.ingresso_entity import IngressoEntity
from .base import Base
from uuid import uuid4


class Ingresso(Base):
    __tablename__ = 'ingresso'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    id_sessao = Column(String(36), ForeignKey('sessao.id'), nullable=False)
    id_setor = Column(String(36), ForeignKey('setor.id'), nullable=False)
    cadeira = Column(String, nullable=True)
    valor = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Ingresso(id={self.id}, cadeira={self.cadeira}, valor={self.valor})>"

    def to_entity(self):
        return IngressoEntity(
            cadeira=self.cadeira,
            id=self.id,
            id_sessao=self.id_sessao,
            id_setor=self.id_setor,
            valor=self.valor
        )
