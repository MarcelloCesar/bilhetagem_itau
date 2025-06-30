import uuid
from sqlalchemy.orm import Session
from src.adapters.sqlalchemy_entities.evento import Evento
from src.adapters.sqlalchemy_entities.sessao import Sessao
from src.adapters.sqlalchemy_entities.setor import Setor
from src.adapters.sqlalchemy_entities.ingresso import Ingresso
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


eventos_id = [str(uuid.uuid4()) for _ in range(10)]
def popular_mock_eventos(session: Session):
    eventos = [
        Evento(id=eventos_id[0], nome="Show de Rock", descricao="Um show incrível de rock com bandas locais."),
        Evento(id=eventos_id[1], nome="Jogo de Futebol", descricao="Partida emocionante entre os times da cidade."),
        Evento(id=eventos_id[2], nome="Peça de Teatro", descricao="Uma peça emocionante sobre a vida urbana."),
        Evento(id=eventos_id[3], nome="Palestra de Tecnologia", descricao="Discussão sobre as últimas tendências em tecnologia."),
        Evento(id=eventos_id[4], nome="Workshop de Fotografia", descricao="Aprenda técnicas de fotografia com profissionais."),
        Evento(id=eventos_id[5], nome="Feira de Livros", descricao="Encontro de autores e leitores com venda de livros."),
        Evento(id=eventos_id[6], nome="Apresentação de Dança", descricao="Uma apresentação vibrante de dança contemporânea."),
        Evento(id=eventos_id[7], nome="Stand-up Comedy", descricao="Noite de risadas com comediantes locais."),
        Evento(id=eventos_id[8], nome="Concerto Clássico", descricao="Uma apresentação de música clássica com orquestra."),
        Evento(id=eventos_id[9], nome="Festival de Comida", descricao="Degustação de pratos de diferentes culturas."),
        Evento(id="1234-5678-90", nome="Mock", descricao="Evento de teste para validação do sistema."),
    ]

    session.add_all(eventos)
    session.commit()


sessoes_id = [str(uuid.uuid4()) for _ in range(5)]
def popular_mock_sessoes(session: Session):
    amanha = (datetime.now() + timedelta(days=1)).date()
    horas_19 = datetime.combine(amanha, datetime.strptime("19:00", "%H:%M").time()).time()
    horas_20 = datetime.combine(amanha, datetime.strptime("20:00", "%H:%M").time()).time()
    horas_21 = datetime.combine(amanha, datetime.strptime("21:00", "%H:%M").time()).time()

    sessoes = [
        Sessao(id=sessoes_id[0], id_evento=eventos_id[0], data=amanha, horario_inicio=horas_19),
        Sessao(id=sessoes_id[1], id_evento=eventos_id[0], data=amanha, horario_inicio=horas_20),
        Sessao(id=sessoes_id[2], id_evento=eventos_id[0], data=amanha, horario_inicio=horas_21),
        Sessao(id=sessoes_id[3], id_evento=eventos_id[1], data=amanha, horario_inicio=horas_19),
        Sessao(id=sessoes_id[4], id_evento=eventos_id[1], data=amanha, horario_inicio=horas_20),
    ]

    session.add_all(sessoes)
    session.commit()


setores_id = [str(uuid.uuid4()) for _ in range(5)]
def popular_mock_setores(session: Session):
    setores = [
        Setor(id=setores_id[0], nome="Setor A", capacidade=5, valor=50.00),
        Setor(id=setores_id[1], nome="Setor B", capacidade=10, valor=75.00),
        Setor(id=setores_id[2], nome="Setor C", capacidade=5, valor=60.00),
        Setor(id=setores_id[3], nome="Arquibancada", capacidade=10, valor=60.00, possui_lugar_marcado=True),
        Setor(id=setores_id[4], nome="Plateia", capacidade=20, valor=100.00, possui_lugar_marcado=True),
        Setor(id="1234-5678-90", nome="Mock Setor", capacidade=50, valor=20.00),
    ]

    session.add_all(setores)
    session.commit()


ingressos_id = [str(uuid.uuid4()) for _ in range(25)]
def popular_mock_ingressos(session: Session):
    ingressos_0 = [
        Ingresso(id=ingressos_id[i],
                 id_sessao=sessoes_id[0],
                 id_setor=setores_id[0], valor=50.00) for i in range(5)
    ]

    ingressos_1 = [
        Ingresso(id=ingressos_id[i + 5],
                 id_sessao=sessoes_id[3],
                 id_setor=setores_id[3], cadeira=f"A{i}", valor=75.00) for i in range(10)
    ]

    ingressos_2 = [
        Ingresso(id=ingressos_id[i + 15],
                 id_sessao=sessoes_id[4],
                 id_setor=setores_id[3], cadeira=f"A{i}", valor=75.00) for i in range(10)
    ]

    for ingresso in ingressos_0 + ingressos_1 + ingressos_2:
        session.add(ingresso)

    session.commit()


engine = create_engine("sqlite:///./service_bilhetagem.db")
session = sessionmaker(bind=engine)()

popular_mock_eventos(session)
popular_mock_sessoes(session)
popular_mock_setores(session)
popular_mock_ingressos(session)
session.close()
