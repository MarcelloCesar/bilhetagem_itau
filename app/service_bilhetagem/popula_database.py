import uuid
from sqlalchemy.orm import Session
from src.adapters.sqlalchemy_entities.evento import Evento
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def popular_mock_eventos(session: Session):
    eventos = [
        Evento(id=str(uuid.uuid4()), nome="Show de Rock", descricao="Um show incrível de rock com bandas locais."),
        Evento(id=str(uuid.uuid4()), nome="Festival de Cinema", descricao="Exibição de filmes independentes e documentários."),
        Evento(id=str(uuid.uuid4()), nome="Peça de Teatro", descricao="Uma peça emocionante sobre a vida urbana."),
        Evento(id=str(uuid.uuid4()), nome="Palestra de Tecnologia", descricao="Discussão sobre as últimas tendências em tecnologia."),
        Evento(id=str(uuid.uuid4()), nome="Workshop de Fotografia", descricao="Aprenda técnicas de fotografia com profissionais."),
        Evento(id=str(uuid.uuid4()), nome="Feira de Livros", descricao="Encontro de autores e leitores com venda de livros."),
        Evento(id=str(uuid.uuid4()), nome="Apresentação de Dança", descricao="Uma apresentação vibrante de dança contemporânea."),
        Evento(id=str(uuid.uuid4()), nome="Stand-up Comedy", descricao="Noite de risadas com comediantes locais."),
        Evento(id=str(uuid.uuid4()), nome="Concerto Clássico", descricao="Uma apresentação de música clássica com orquestra."),
        Evento(id=str(uuid.uuid4()), nome="Festival de Comida", descricao="Degustação de pratos de diferentes culturas."),
        Evento(id="1234-5678-90", nome="Mock", descricao="Evento de teste para validação do sistema."),
    ]

    session.add_all(eventos)
    session.commit()


engine = create_engine("sqlite:///./service_bilhetagem.db")
session = sessionmaker(bind=engine)()

popular_mock_eventos(session)
