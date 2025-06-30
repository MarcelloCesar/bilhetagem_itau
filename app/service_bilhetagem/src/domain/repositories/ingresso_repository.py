from ..entities.ingresso_entity import IngressoEntity


class IngressoRepository:
    def get_ingresso_por_id(self, id_ingresso: str) -> IngressoEntity:
        """
        Busca um ingresso pelo ID.

        :param id_ingresso: ID do ingresso a ser buscado.
        :return: IngressoEntity com os detalhes do ingresso encontrado.
        """
        raise NotImplementedError("Este método deve ser implementado por subclasses.")

    def get_ingresso_disponivel_para_sessao_e_setor(self,
                                                    id_sessao: str,
                                                    id_setor: str) -> IngressoEntity:
        """
        Busca um ingresso disponível para uma sessão e setor específicos.

        :param id_sessao: ID da sessão do evento.
        :param id_setor: ID do setor do evento.
        :return: IngressoEntity com os detalhes do ingresso encontrado.
        """
        raise NotImplementedError("Este método deve ser implementado por subclasses.")
