from dataclasses import dataclass


@dataclass
class ReservaEntity:
    id: str
    id_ingresso: str
    id_cliente: str
    valor: float
    data_hora_reserva: int
    data_hora_expiracao: int
    situacao: str
