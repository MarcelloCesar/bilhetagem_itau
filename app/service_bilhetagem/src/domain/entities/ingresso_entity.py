from dataclasses import dataclass


@dataclass
class IngressoEntity:
    id: str
    id_sessao: str
    id_setor: str
    cadeira: str
    valor: float
