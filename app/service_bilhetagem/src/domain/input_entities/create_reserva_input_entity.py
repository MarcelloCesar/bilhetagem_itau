from pydantic import BaseModel, Field, ConfigDict


class CreateReservaRequest(BaseModel):
    id_sessao: str = Field(
        min_length=36, max_length=36,
        description="ID da sessao de evento para o qual a reserva está sendo criada"
    )

    id_setor: str = Field(
        min_length=36, max_length=36,
        description="ID do setor onde a reserva está sendo feita"
    )

    cadeira: str | None = Field(
        min_length=1, max_length=10,
        default=None,
        description="Número da cadeira para a qual a reserva está sendo feita"
    )

    id_cliente: str = Field(
        max_length=36,
        description="ID do usuário que está fazendo a reserva"
    )

    model_config = ConfigDict(
        str_strip_whitespace=True
    )
