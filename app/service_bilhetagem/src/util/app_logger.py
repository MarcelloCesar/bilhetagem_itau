import logging
import json
import sys
from datetime import datetime
from contextvars import ContextVar

trace_id_ctx = ContextVar("trace_id", default=None)


class JsonFormatter(logging.Formatter):
    def format(self, record):
        trace_id = getattr(record, "trace_id", None) or trace_id_ctx.get()

        log_record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
            "function": record.funcName,
            "line": record.lineno,
        }

        if trace_id:
            log_record["trace_id"] = trace_id

        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_record)


class AppLogger:
    LEVEL = "INFO"
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AppLogger, cls).__new__(cls)
            cls._instance._initialize_logger(*args, **kwargs)
        return cls._instance

    def _initialize_logger(self, name="app"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.LEVEL)
        self.logger.propagate = False

        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(JsonFormatter())
            self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger

    def set_trace_id(self, trace_id: str):
        trace_id_ctx.set(trace_id)
