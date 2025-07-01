from sqlalchemy import Column, String, ForeignKey, Float, DateTime
from ...domain.entities.reserva_entity import ReservaEntity
from .base import Base
from uuid import uuid4


class Reserva(Base):
    __tablename__ = 'reserva'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    id_ingresso = Column(String(36), ForeignKey('ingresso.id'), nullable=False)
    id_cliente = Column(String(36), nullable=False)
    valor = Column(Float, nullable=False)
    data_hora_reserva = Column(DateTime, nullable=False)
    data_hora_expiracao = Column(DateTime, nullable=False)
    situacao = Column(String, nullable=False)

    def __repr__(self):
        return f"<Reserva(id={self.id}, valor={self.valor}, situacao={self.situacao})>"

    def to_entity(self):
        return ReservaEntity(
            id=self.id,
            id_ingresso=self.id_ingresso,
            id_cliente=self.id_cliente,
            valor=self.valor,
            data_hora_reserva=self.data_hora_reserva,
            data_hora_expiracao=self.data_hora_expiracao,
            situacao=self.situacao
        )
