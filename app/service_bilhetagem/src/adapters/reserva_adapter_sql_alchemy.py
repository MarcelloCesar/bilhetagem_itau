from ..domain.repositories.reserva_repository import ReservaRepository
from ..services.database_service import DatabaseService
from ..domain.entities.reserva_entity import ReservaEntity
from ..adapters.sqlalchemy_entities.reserva import Reserva
from sqlalchemy.exc import SQLAlchemyError
from ..util.app_logger import AppLogger

logger = AppLogger().get_logger()


class ReservaAdapterSQLAlchemy(ReservaRepository):
    def __init__(self, database: DatabaseService = None):
        self.database = database or DatabaseService()

    def create_nova_reserva(self, reserva: ReservaEntity) -> ReservaEntity:
        try:
            session = self.database.get_session()
            nova_reserva = Reserva(
                id_ingresso=reserva.id_ingresso,
                id_cliente=reserva.id_cliente,
                valor=reserva.valor,
                data_hora_reserva=reserva.data_hora_reserva,
                data_hora_expiracao=reserva.data_hora_expiracao,
                situacao=reserva.situacao
            )
            session.add(nova_reserva)
            session.commit()
            session.refresh(nova_reserva)
            session.close()

            reserva.id = nova_reserva.id
            return reserva

        except SQLAlchemyError as e:
            logger.error(f"Erro ao buscar reserva por ID: {e}")
            raise e
