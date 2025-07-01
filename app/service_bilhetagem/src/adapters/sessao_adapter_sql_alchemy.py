from ..domain.repositories.sessao_repository import SessaoRepository
from ..services.database_service import DatabaseService
from ..domain.dtos.sessao_ingressos_disponiveis_dto import SessaoIngressosDisponiveisDTO
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, func, and_, not_, exists
from ..adapters.sqlalchemy_entities.sessao import Sessao
from ..adapters.sqlalchemy_entities.ingresso import Ingresso
from ..adapters.sqlalchemy_entities.reserva import Reserva
from ..adapters.sqlalchemy_entities.setor import Setor
from sqlalchemy.orm import aliased
from datetime import datetime
from ..util.app_logger import AppLogger

logger = AppLogger().get_logger()


class SessaoAdapterSQLAlchemy(SessaoRepository):
    def __init__(self, database: DatabaseService = None):
        self.database = database or DatabaseService()

    def get_dados_sessoes_ativas_para_o_evento(self, id_evento: str):
        try:
            logger.debug(f"Buscando sessões ativas para o evento com ID: {id_evento}")
            now = datetime.now()
            session: Session = self.database.get_session()
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
                select(
                    Sessao.id,
                    Sessao.data,
                    Sessao.horario_inicio,
                    Setor.id,
                    Setor.nome,
                    Setor.possui_lugar_marcado,
                    func.count().label("ingressos_disponiveis"),
                    func.group_concat(Ingresso.cadeira).label("cadeiras_disponiveis")
                )
                .join(Sessao, Sessao.id == Ingresso.id_sessao)
                .join(Setor, Setor.id == Ingresso.id_setor)
                .where(
                    Sessao.id_evento == id_evento,
                    not_(exists(subquery_reservas_ativas))
                )
                .group_by(Sessao.id, Sessao.data, Sessao.horario_inicio, Setor.nome, Setor.possui_lugar_marcado)
            )

            result = session.execute(query).all()
            session.close()

            logger.debug(f"Sessões ativas encontradas para o evento {id_evento}: {result}")
            return [
                SessaoIngressosDisponiveisDTO(
                    id_sessao=row[0],
                    data_sessao=row[1],
                    horario_inicio=row[2],
                    setor_id=row[3],
                    setor_nome=row[4],
                    possui_lugar_marcado=row[5],
                    ingressos_disponiveis=row[6],
                    cadeiras_disponiveis=row[7]
                ) for row in result
            ]

        except SQLAlchemyError as e:
            logger.error(f"Erro ao obter dados das sessões ativas para o evento {id_evento}: {e}")
            raise e
