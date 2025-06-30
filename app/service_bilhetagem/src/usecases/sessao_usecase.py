from ..domain.repositories.sessao_repository import SessaoRepository


class SessaoUseCase:
    def __init__(self, sessao_repository: SessaoRepository):
        self.repository = sessao_repository

    def get_dados_sessoes_ativas_para_o_evento(self, id_evento: str):
        sessoes = self.repository.\
            get_dados_sessoes_ativas_para_o_evento(id_evento)
        if not sessoes:
            return {"error": "Nenhuma sessão ativa encontrada para o evento"}

        return {
            "sessoes": [
                {
                    "id_sessao": sessao.id_sessao,
                    "data_sessao": sessao.data_sessao,
                    "horario_inicio": sessao.horario_inicio,
                    "setores": sessao.setor,
                    "possui_lugar_marcado": sessao.possui_lugar_marcado,
                    "ingressos_disponiveis": sessao.ingressos_disponiveis,
                    "cadeiras_disponiveis": sessao.cadeiras_disponiveis
                } for sessao in sessoes
            ]
        }
