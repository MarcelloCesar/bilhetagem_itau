from dataclasses import dataclass
from datetime import datetime


@dataclass
class ReservaEntity:
    id: str
    id_ingresso: str
    id_cliente: str
    valor: float
    data_hora_reserva: datetime
    data_hora_expiracao: datetime
    situacao: str

    def __post_init__(self):
        if not isinstance(self.data_hora_reserva, datetime):
            raise TypeError("data_hora_reserva deve ser do tipo datetime")
        if not isinstance(self.data_hora_expiracao, datetime):
            raise TypeError("data_hora_expiracao deve ser do tipo datetime")
        if self.data_hora_expiracao <= self.data_hora_reserva:
            raise ValueError("data_hora_expiracao deve ser maior que data_hora_reserva")
        if self.situacao not in ["ANALISE", "CONFIRMADA"]:
            raise ValueError("situacao deve ser 'ANALISE' ou 'CONFIRMADA'")
