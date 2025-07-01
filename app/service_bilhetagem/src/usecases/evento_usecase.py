from ..domain.repositories.evento_repository import EventoRepository
from ..util.app_logger import AppLogger

logger = AppLogger().get_logger()


class EventoUseCase:
    def __init__(self, evento_repository: EventoRepository):
        self.repository = evento_repository

    def get_dados_evento(self, id_evento: str):
        """
        Obtém os dados de um evento específico pelo ID.
        :param id_evento: ID do evento a ser buscado.
        :return: Dados do evento ou mensagem de erro se não encontrado.
        """
        logger.debug(f"Buscando dados do evento com ID: {id_evento}")
        evento = self.repository.get_dados_evento_por_id(id_evento)
        if not evento:
            return {"error": "Evento não encontrado"}

        logger.debug(f"Evento encontrado: {evento}")
        return {
            "id": evento.id,
            "nome": evento.nome,
            "descricao": str(evento.descricao)
        }

    def get_lista_eventos(self):
        """
        Obtém uma lista de todos os eventos disponíveis.
        :return: Lista de eventos ou mensagem de erro se nenhum evento for encontrado.
        """
        logger.debug("Buscando lista de eventos")
        eventos = self.repository.get_lista_eventos()
        if not eventos:
            return {"error": "Nenhum evento encontrado"}

        logger.debug(f"Eventos encontrados: {eventos}")
        return [
            {
                "id": evento.id,
                "nome": evento.nome,
                "descricao": str(evento.descricao) if evento.descricao else None
            } for evento in eventos
        ]
