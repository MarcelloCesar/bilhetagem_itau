from dataclasses import dataclass


@dataclass
class SessaoIngressosDisponiveisDTO:
    id_sessao: str
    data_sessao: str
    horario_inicio: str
    setor: str
    possui_lugar_marcado: bool
    ingressos_disponiveis: int
    cadeiras_disponiveis: str
