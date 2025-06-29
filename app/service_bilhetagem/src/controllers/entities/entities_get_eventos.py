from pydantic import BaseModel, Field, ConfigDict
from typing import List


class GetEventosResponse(BaseModel):
    idEvento: str
    nomeEvento: str

    model_config = ConfigDict(
        str_strip_whitespace=True
    )
