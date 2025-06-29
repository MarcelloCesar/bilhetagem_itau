from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv


class DatabaseService:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls, *args, **kwargs)
            cls.instance._initialize()
        return cls.instance

    def _initialize(self):
        database_path = getenv("DB_BILHETAGEM_PATH", "")
        self.database_url = "sqlite:///./" + database_path
        self.engine = create_engine(self.database_url, echo=False)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        """Retorna uma nova sessão do banco de dados."""
        return self.SessionLocal()

    def close(self):
        """Fecha a conexão com o banco de dados."""
        self.engine.dispose()
        self.instance = None
