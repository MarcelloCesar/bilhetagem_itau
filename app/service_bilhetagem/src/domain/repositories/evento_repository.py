from ..entities.evento_entity import EventoEntity


class EventoRepository:
    def get_dados_evento_por_id(self, id_evento: str) -> EventoEntity:
        """
        Obtém os dados de um evento específico pelo ID.
        :param id_evento: ID do evento a ser buscado.
        :return: EventoEntity contendo os dados do evento.
        """
        raise NotImplementedError("Este método deve ser implementado por subclasses.") # pragma: no cover

    def get_lista_eventos(self) -> list[EventoEntity]:
        """
        Obtém a lista de todos os eventos
        :return: Lista de EventoEntity contendo os dados de todos os eventos.
        """
        raise NotImplementedError("Este método deve ser implementado por subclasses.") # pragma: no cover
