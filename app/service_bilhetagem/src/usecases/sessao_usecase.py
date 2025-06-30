from ..domain.repositories.sessao_repository import SessaoRepository
from ..util.app_logger import AppLogger

logger = AppLogger().get_logger()


class SessaoUseCase:
    def __init__(self, sessao_repository: SessaoRepository):
        self.repository = sessao_repository

    def get_dados_sessoes_ativas_para_o_evento(self, id_evento: str):
        logger.debug(f"Buscando sessões ativas para o evento com ID: {id_evento}")
        sessoes = self.repository.\
            get_dados_sessoes_ativas_para_o_evento(id_evento)
        if not sessoes:
            return {"error": "Nenhuma sessão ativa encontrada para o evento"}

        logger.debug(f"Sessões ativas encontradas: {sessoes}")
        return {
            "sessoes": [
                {
                    "id_sessao": sessao.id_sessao,
                    "data_sessao": sessao.data_sessao,
                    "horario_inicio": sessao.horario_inicio,
                    "setor": {"id": sessao.setor_id,
                              "nome": sessao.setor_nome},
                    "possui_lugar_marcado": sessao.possui_lugar_marcado,
                    "ingressos_disponiveis": sessao.ingressos_disponiveis,
                    "cadeiras_disponiveis": sessao.cadeiras_disponiveis
                } for sessao in sessoes
            ]
        }
