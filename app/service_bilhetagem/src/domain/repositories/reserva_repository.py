from ..entities.reserva_entity import ReservaEntity


class ReservaRepository:
    def create_nova_reserva(self, reserva: ReservaEntity) -> ReservaEntity:
        """
        Cria uma nova reserva.

        :param reserva: Objeto ReservaEntity contendo os detalhes da reserva.
        :return: ReservaEntity com os detalhes da reserva criada.
        """
        raise NotImplementedError("Este método deve ser implementado por subclasses.") # pragma: no cover
