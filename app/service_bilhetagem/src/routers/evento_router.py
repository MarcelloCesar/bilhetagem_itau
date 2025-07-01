from fastapi import APIRouter
from src.controllers.http.eventos_http_controller import (
    http_get_dados_evento, http_get_lista_eventos
)
from src.controllers.http.sessoes_http_controller import (
    http_get_sessoes_disponiveis_evento
)

router = APIRouter(prefix="/eventos")


@router.get("/")
async def rota_get_lista_eventos():
    return http_get_lista_eventos()


@router.get("/{id_evento}")
async def rota_get_evento(id_evento: str):
    return http_get_dados_evento(id_evento)


@router.get("/{id_evento}/sessoes")
async def rota_get_sessoes_disponiveis_evento(id_evento: str):
    return http_get_sessoes_disponiveis_evento(id_evento)
