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
import logging

logger = logging.getLogger(__name__)


class SessaoAdapterSQLAlchemy(SessaoRepository):
    def __init__(self, database: DatabaseService = None):
        self.database = database or DatabaseService()

    def get_dados_sessoes_ativas_para_o_evento(self, id_evento: str):
        try:
            session: Session = self.database.get_session()
            subquery_reservas_ativas = (
                select(Reserva.id)
                .where(
                    and_(
                        Reserva.id_ingresso == Ingresso.id,
                        func.current_timestamp().between(
                            Reserva.data_hora_reserva,
                            Reserva.data_hora_expiracao
                        )
                    )
                )
            )

            query = (
                select(
                    Sessao.id,
                    Sessao.data,
                    Sessao.horario_inicio,
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

            return [
                SessaoIngressosDisponiveisDTO(
                    id_sessao=row[0],
                    data_sessao=row[1],
                    horario_inicio=row[2],
                    setor=row[3],
                    possui_lugar_marcado=row[4],
                    ingressos_disponiveis=row[5],
                    cadeiras_disponiveis=row[6]
                ) for row in result
            ]

        except SQLAlchemyError as e:
            logger.error(f"Erro ao obter dados das sessões ativas para o evento {id_evento}: {e}")
            raise e
