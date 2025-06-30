from dataclasses import dataclass


@dataclass
class SetorEntity:
    id: str
    nome: str
    capacidade: int
    valor: float
    possui_lugar_marcado: bool = False

    def __post_init__(self):
        if self.preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if self.capacidade <= 0:
            raise ValueError("A capacidade deve ser um número positivo.")
