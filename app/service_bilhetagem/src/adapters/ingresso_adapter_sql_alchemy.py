from ..domain.repositories.ingresso_repository import IngressoRepository
from ..services.database_service import DatabaseService
from ..domain.entities.ingresso_entity import IngressoEntity
from ..adapters.sqlalchemy_entities.ingresso import Ingresso
from ..adapters.sqlalchemy_entities.reserva import Reserva
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, and_, not_, exists
from datetime import datetime
from ..util.app_logger import AppLogger

logger = AppLogger().get_logger()


class IngressoAdapterSQLAlchemy(IngressoRepository):
    def __init__(self, database: DatabaseService = None):
        self.database = database or DatabaseService()

    def get_ingresso_por_id(self, id_ingresso: str) -> IngressoEntity:
        try:
            logger.debug(f"Buscando ingresso com ID: {id_ingresso}")
            session = self.database.get_session()
            ingresso = session.query(Ingresso).\
                filter_by(id=id_ingresso).first()
            session.close()

            logger.debug(f"Ingresso encontrado: {ingresso}")
            return ingresso.to_entity() if ingresso else None

        except SQLAlchemyError as e:
            logger.exception(f"Erro ao obter dados do ingresso com ID {id_ingresso}: {e}")
            session.rollback()
            raise e

    def get_ingresso_disponivel_para_sessao_e_setor(
            self, id_sessao: str, id_setor: str, cadeira: str = None) -> IngressoEntity:
        try:
            logger.debug(f"Buscando ingresso disponível para a sessão {id_sessao} e setor {id_setor}")
            now = datetime.now()
            session = self.database.get_session()
            subquery_reservas_ativas = (
                select(Reserva.id)
                .where(
                    and_(
                        Reserva.id_ingresso == Ingresso.id,
                        Reserva.data_hora_reserva <= now,
                        Reserva.data_hora_expiracao >= now
                    )
                )
            )

            query = (
                select(Ingresso)
                .where(
                    and_(
                        Ingresso.id_sessao == id_sessao,
                        Ingresso.id_setor == id_setor,
                        Ingresso.cadeira == cadeira if cadeira else True,
                        not_(exists(subquery_reservas_ativas))
                    )
                )
                .limit(1)
            )

            result: list[Ingresso] = session.execute(query).first()
            session.close()

            logger.debug(f"Ingresso disponível encontrado: {result}")
            return result[0].to_entity() if result else None

        except SQLAlchemyError as e:
            logger.exception(f"Erro ao obter ingresso disponível para a sessão {id_sessao} e setor {id_setor}: {e}")
            session.rollback()
            raise e
