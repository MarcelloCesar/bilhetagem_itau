from ..entities.setor_entity import SetorEntity


class SetorRepository:
    def get_setor_por_id(self, id_setor: str) -> SetorEntity:
        """
        Busca um setor pelo ID.

        :param id_ingresso: ID do setor a ser buscado.
        :return: SetorEntity com os detalhes do setor encontrado.
        """
        raise NotImplementedError("Este método deve ser implementado por subclasses.")
