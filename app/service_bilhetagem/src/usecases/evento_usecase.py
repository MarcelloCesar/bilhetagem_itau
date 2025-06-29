from ..domain.repositories.evento_repository import EventoRepository


class EventoUseCase:
    def __init__(self, evento_repository: EventoRepository):
        self.repository = evento_repository

    def get_dados_evento(self, id_evento: str):
        evento = self.repository.get_dados_evento_por_id(id_evento)
        if not evento:
            return {"error": "Evento não encontrado"}

        return {
            "id": evento.id,
            "nome": evento.nome
        }

    def get_lista_eventos(self):
        eventos = self.repository.get_lista_eventos()
        if not eventos:
            return {"error": "Nenhum evento encontrado"}

        return [
            {
                "id": evento.id,
                "nome": evento.nome
            } for evento in eventos
        ]
