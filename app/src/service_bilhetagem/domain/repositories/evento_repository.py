from ..entities.evento_entity import EventoEntity


class EventoRepository:
    def get_dados_evento_por_id(self, id_evento: str) -> EventoEntity:
        """
        Obtém os dados de um evento específico pelo ID.
        """
        raise NotImplementedError("Método não implementado")

    def get_lista_eventos(self) -> list[EventoEntity]:
        """
        Obtém a lista de todos os eventos
        """
        raise NotImplementedError("Método não implementado")
