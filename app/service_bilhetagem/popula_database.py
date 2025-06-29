import uuid
from sqlalchemy.orm import Session
from src.adapters.sqlalchemy_entities.evento import Evento
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def popular_mock_eventos(session: Session):
    eventos = [
        Evento(id=str(uuid.uuid4()), nome="Show de Rock"),
        Evento(id=str(uuid.uuid4()), nome="Festival de Cinema"),
        Evento(id=str(uuid.uuid4()), nome="Peça de Teatro"),
        Evento(id=str(uuid.uuid4()), nome="Palestra de Tecnologia"),
        Evento(id=str(uuid.uuid4()), nome="Workshop de Fotografia"),
        Evento(id=str(uuid.uuid4()), nome="Feira de Livros"),
        Evento(id=str(uuid.uuid4()), nome="Apresentação de Dança"),
        Evento(id=str(uuid.uuid4()), nome="Stand-up Comedy"),
        Evento(id=str(uuid.uuid4()), nome="Concerto Clássico"),
        Evento(id=str(uuid.uuid4()), nome="Festival de Comida"),
    ]

    session.add_all(eventos)
    session.commit()


engine = create_engine("sqlite:///./service_bilhetagem.db")
session = sessionmaker(bind=engine)()

popular_mock_eventos(session)
