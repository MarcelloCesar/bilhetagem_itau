from ..domain.repositories.evento_repository import EventoRepository
from ..services.database_service import DatabaseService
from ..adapters.sqlalchemy_entities.evento import Evento
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging

logger = logging.getLogger(__name__)


class EventoAdapterSQLAlchemy(EventoRepository):
    def __init__(self, database: DatabaseService = None):
        self.database = database or DatabaseService()

    def get_dados_evento_por_id(self, id_evento: str):
        try:
            session: Session = self.database.get_session()
            evento = session.query(Evento).\
                filter_by(id=id_evento).first()
            session.close()
            return evento.to_entity() if evento else None

        except SQLAlchemyError as e:
            logger.exception(f"Erro ao obter dados do evento com ID {id_evento}: {e}")
            session.rollback()
            raise e

    def get_lista_eventos(self):
        try:
            session: Session = self.database.get_session()
            eventos = session.query(Evento).all()
            session.close()
            return [evento.to_entity() for evento in eventos]

        except SQLAlchemyError as e:
            logger.exception(f"Erro ao obter lista de eventos: {e}")
            session.rollback()
            raise e
