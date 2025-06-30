from ...usecases.sessao_usecase import SessaoUseCase
from ...adapters.sessao_adapter_sql_alchemy import (
    SessaoAdapterSQLAlchemy
)


def http_get_sessoes_disponiveis_evento(id_evento: str):
    usecase = SessaoUseCase(sessao_repository=SessaoAdapterSQLAlchemy())
    return usecase.get_dados_sessoes_ativas_para_o_evento(id_evento)
