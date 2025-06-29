from ...usecases.evento_usecase import EventoUseCase
from ...adapters.evento_adapter_sql_alchemy import (
    EventoAdapterSQLAlchemy
)


def http_get_dados_evento(id_evento: str):
    usecase = EventoUseCase(evento_repository=EventoAdapterSQLAlchemy())
    return usecase.get_dados_evento(id_evento)


def http_get_lista_eventos():
    usecase = EventoUseCase(evento_repository=EventoAdapterSQLAlchemy())
    return usecase.get_lista_eventos()
