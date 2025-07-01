class RequestValidationException(Exception):
    def __init__(self, errors: list[dict]):
        self.errors = errors
        super().__init__("Erro de validação na requisição.")
