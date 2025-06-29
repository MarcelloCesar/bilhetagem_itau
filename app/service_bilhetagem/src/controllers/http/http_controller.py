from functools import wraps
from json import JSONDecodeError
from src.exceptions.business_exception import BusinessException
from src.util.http_responses import ResponsesHTTP
from aws_lambda_powertools import Logger
from pydantic import ValidationError

logger = Logger()


def http_controller(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BusinessException as exc:
            return ResponsesHTTP.response_409({"message": str(exc)})
        except JSONDecodeError:
            return ResponsesHTTP.\
                response_400("Dados de entrada deve ser um json")
        except ValidationError as exc:
            logger.info("Validation error: " + str(exc))
            return ResponsesHTTP.response_400("Verifique os dados informados")
        except KeyError as exc:
            return ResponsesHTTP.response_400(str(exc))
        except Exception as exc:
            logger.exception(exc)
            return ResponsesHTTP.response_500(str(exc))
    return wrapper
