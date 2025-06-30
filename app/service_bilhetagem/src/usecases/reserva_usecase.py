from ..domain.repositories.reserva_repository import ReservaRepository
from ..domain.repositories.setor_repository import SetorRepository
from ..domain.repositories.ingresso_repository import IngressoRepository
from ..domain.input_entities.create_reserva_input_entity import \
    CreateReservaRequest
from ..domain.entities.reserva_entity import ReservaEntity
from datetime import datetime, timedelta
from uuid import uuid4


class ReservaUseCase:

    def __init__(self, reserva_repository: ReservaRepository,
                 setor_repository: SetorRepository,
                 ingresso_repository: IngressoRepository):
        self.reserva_repository = reserva_repository
        self.minutos_expiracao_reserva = 10  # no futuro, recuperar de configuração
        self.setor_repository = setor_repository
        self.ingresso_repository = ingresso_repository

    def create_nova_reserva(self, request: CreateReservaRequest):
        setor_selecionado = self.setor_repository.\
            get_setor_por_id(request.id_setor)
        if not setor_selecionado:
            return {"error": "O setor selecionado não existe"}

        if setor_selecionado.possui_lugar_marcado and \
                not request.cadeira:
            return {
                "error": "Para setores com lugares marcados, "
                         "é necessário informar a cadeira"
            }
        ingresso_disponivel = self.ingresso_repository.\
            get_ingresso_disponivel_para_sessao_e_setor(
                id_sessao=request.id_sessao,
                id_setor=request.id_setor
            )
        if not ingresso_disponivel:
            return {"error": "Não há ingressos disponíveis para a sessão e setor selecionados"}

        nova_reserva = ReservaEntity(
            id=str(uuid4()),
            id_cliente=request.id_cliente,
            valor=setor_selecionado.valor,
            data_hora_reserva=datetime.now(),
            data_hora_expiracao=datetime.now() +
            timedelta(minutes=self.minutos_expiracao_reserva),
            situacao="ATIVA",
            id_ingresso=ingresso_disponivel.id
        )
        reserva = self.reserva_repository.create_nova_reserva(nova_reserva)
        return reserva.id
