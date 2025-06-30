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


def http_post_criar_reserva(headers: dict, body):
    try:
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
        token = authorization.split(" ")[1]
        authorization = jwt.decode(token, options={"verify_signature": False})

        id_cliente = authorization.get("id_cliente")
        if not id_cliente:
            raise RequestValidationException(
                errors=[{"campo": "Authorization",
                         "mensagem": "Token não contém id_cliente"}]
            )

        body["id_cliente"] = id_cliente
        request_body = CreateReservaRequest(**body)
        return usecase.create_nova_reserva(request_body)
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
