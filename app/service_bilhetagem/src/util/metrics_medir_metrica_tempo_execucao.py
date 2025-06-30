import time
from functools import wraps
from .app_logger import AppLogger

logger = AppLogger().get_logger()


def medir_metrica_tempo_execucao(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        duracao = fim - inicio
        logger.info(f"[{func.__name__}] Tempo de execução: {duracao:.4f} segundos")
        return resultado
    return wrapper
