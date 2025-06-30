from ...usecases.evento_usecase import EventoUseCase
from ...adapters.evento_adapter_sql_alchemy import (
    EventoAdapterSQLAlchemy
)
from ...util.app_logger import AppLogger
from ...util.metrics_medir_metrica_tempo_execucao import medir_metrica_tempo_execucao

logger = AppLogger().get_logger()


@medir_metrica_tempo_execucao
def http_get_dados_evento(id_evento: str):
    logger.debug("Iniciando controller http_get_dados_evento")
    logger.info(f"Buscando dados do evento {id_evento}")
    usecase = EventoUseCase(evento_repository=EventoAdapterSQLAlchemy())

    resultado = usecase.get_dados_evento(id_evento)
    logger.info(f"Retornando dados: {resultado}")
    return resultado


@medir_metrica_tempo_execucao
def http_get_lista_eventos():
    logger.debug("Iniciando controller http_get_lista_eventos")
    logger.info("Iniciando listagem de eventos")
    usecase = EventoUseCase(evento_repository=EventoAdapterSQLAlchemy())

    resultado = usecase.get_lista_eventos()
    logger.info(f"Retornando dados: {resultado}")
    return resultado
