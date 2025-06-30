from dataclasses import dataclass


@dataclass
class SessaoEntity:
    id: str
    id_evento: str
    data: str
    horario_inicio: str
