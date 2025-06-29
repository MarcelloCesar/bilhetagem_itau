from pydantic import BaseModel, Field, ConfigDict
from typing import List


class GetDadosEventoResponse(BaseModel):
    idEvento: str
    nomeEvento: str
    descricaoEvento: str | None = Field(default=None, description="Descrição do evento")

    model_config = ConfigDict(
        str_strip_whitespace=True
    )


class GetListaEventosResponse(BaseModel):
    eventos: List[GetDadosEventoResponse]

    model_config = ConfigDict(
        str_strip_whitespace=True
    )
