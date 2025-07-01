from ...usecases.sessao_usecase import SessaoUseCase
from ...adapters.sessao_adapter_sql_alchemy import (
    SessaoAdapterSQLAlchemy
)
from ...util.app_logger import AppLogger
from ...util.metrics_medir_metrica_tempo_execucao import \
    medir_metrica_tempo_execucao

logger = AppLogger().get_logger()


@medir_metrica_tempo_execucao
def http_get_sessoes_disponiveis_evento(id_evento: str):
    try:
        logger.debug("Iniciando controller http_get_sessoes_disponiveis_evento")
        logger.info(f"Iniciando busca de sessoes disponiveis, evento: {id_evento}")
        usecase = SessaoUseCase(sessao_repository=SessaoAdapterSQLAlchemy())

        resultado = usecase.get_dados_sessoes_ativas_para_o_evento(id_evento)
        logger.info(f"Retornando dados: {resultado}")
        return resultado
    except Exception as e:
        logger.exception(e)
        return {"error": "Erro desconhecido"}
