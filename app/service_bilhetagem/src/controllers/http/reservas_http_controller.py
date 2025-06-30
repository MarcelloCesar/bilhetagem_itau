from ...usecases.reserva_usecase import ReservaUseCase
from ...adapters.reserva_adapter_sql_alchemy import ReservaAdapterSQLAlchemy
from ...adapters.setor_adapter_sql_alchemy import SetorAdapterSQLAlchemy
from ...adapters.ingresso_adapter_sql_alchemy import IngressoAdapterSQLAlchemy
from ...domain.input_entities.create_reserva_input_entity import (
    CreateReservaRequest
)
from pydantic import ValidationError
from src.domain.exceptions.request_validation_exception import \
    RequestValidationException
import jwt
from ...util.app_logger import AppLogger
from ...util.metrics_medir_metrica_tempo_execucao import medir_metrica_tempo_execucao

logger = AppLogger().get_logger()


@medir_metrica_tempo_execucao
def http_post_criar_reserva(headers: dict, body):
    try:
        logger.debug("Iniciando controller http_post_criar_reserva")
        logger.info("Iniciando criacao de reserva")
        usecase = ReservaUseCase(
            reserva_repository=ReservaAdapterSQLAlchemy(),
            setor_repository=SetorAdapterSQLAlchemy(),
            ingresso_repository=IngressoAdapterSQLAlchemy()
        )
        authorization: str = headers.get("authorization", "")
        if not authorization:
            raise RequestValidationException(
                errors=[{"campo": "Authorization",
                         "mensagem": "Header não informado"}]
            )

        logger.debug("Iniciando validação do token")
        token = authorization.split(" ")[1]
        authorization = jwt.decode(token, options={"verify_signature": False})

        id_cliente = authorization.get("id_cliente")
        logger.debug(f"Id do cliente obtido do token: {id_cliente}")
        if not id_cliente:
            raise RequestValidationException(
                errors=[{"campo": "Authorization",
                         "mensagem": "Token não contém id_cliente"}]
            )

        body["id_cliente"] = id_cliente

        logger.debug("Criando objeto de requisição")
        request_body = CreateReservaRequest(**body)

        logger.debug("Iniciando criação da nova reserva")
        resultado = usecase.create_nova_reserva(request_body)

        logger.info(f"Retornando dados: {resultado}")
        return resultado

    except ValidationError as e:
        raise RequestValidationException(
            errors=[
                {
                    "campo": ".".join(str(loc) for loc in err["loc"]),
                    "mensagem": err["msg"]
                }
                for err in e.errors()
            ]
        )

    except jwt.PyJWTError as e:
        raise RequestValidationException(
            errors=[{"campo": "Authorization",
                     "mensagem": f"Token inválido: {str(e)}"}]
        )

    except Exception as e:
        logger.exception(e)
        return
