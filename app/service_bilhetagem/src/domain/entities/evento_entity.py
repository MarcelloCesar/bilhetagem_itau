from dataclasses import dataclass


@dataclass
class EventoEntity:
    id: str
    nome: str
    descricao: str = None
