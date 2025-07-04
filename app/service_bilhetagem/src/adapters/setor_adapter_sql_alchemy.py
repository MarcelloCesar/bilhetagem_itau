from ..domain.repositories.setor_repository import SetorRepository
from ..services.database_service import DatabaseService
from ..domain.entities.setor_entity import SetorEntity
from ..adapters.sqlalchemy_entities.setor import Setor
from sqlalchemy.exc import SQLAlchemyError
from ..util.app_logger import AppLogger

logger = AppLogger().get_logger()


class SetorAdapterSQLAlchemy(SetorRepository):
    def __init__(self, database: DatabaseService = None):
        self.database = database or DatabaseService()

    def get_setor_por_id(self, id_setor: str) -> SetorEntity:
        try:
            logger.debug(f"Buscando setor com ID: {id_setor}")
            session = self.database.get_session()
            setor = session.query(Setor).\
                filter_by(id=id_setor).first()
            session.close()

            logger.debug(f"Setor encontrado: {setor}")
            return setor.to_entity() if setor else None

        except SQLAlchemyError as e:
            logger.exception(f"Erro ao obter dados do setor com ID {id_setor}: {e}")
            session.rollback()
            raise e
