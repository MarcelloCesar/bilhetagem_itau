from ..dtos.sessao_ingressos_disponiveis_dto import (
    SessaoIngressosDisponiveisDTO
)


class SessaoRepository:
    def get_dados_sessoes_ativas_para_o_evento(self, id_evento: str) -> list[SessaoIngressosDisponiveisDTO]:
        """
        Obtém os dados das sessões ativas para um evento específico.
        :param id_evento: ID do evento para o qual as sessões ativas serão buscadas.
        :return: Lista de SessaoIngressosDisponiveisDTO contendo os dados das sessões ativas.
        """
        raise NotImplementedError("Método não implementado") # pragma: no cover
