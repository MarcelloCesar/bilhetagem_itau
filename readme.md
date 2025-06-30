# Projeto de Bilhetagem

Este projeto implementa um sistema de bilhetagem com funcionalidades de solicitação, reserva e compra de ingressos, além da oferta de produtos adicionais como pipoca, refrigerante, chocolate etc durante o processo de compra.

---

## Como rodar o projeto

#### Clone o repositório
```bash
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_PROJETO>
```


#### Crie o ambiente virtual
```bash
python -m venv venv
source venv/Scripts/activate  # git bash ou Linux
```


#### Instale as dependências em ambiente de testes
```bash
pip install -r app/requirements-test.txt
```



#### Crie o banco de dados
```bash
sh init_databases.sh
```

#### Inicie os servidores
```bash
sh start_servers.sh
```

---

## Como rodar os testes
Os testes estao configurados em pytest.ini, tendo a opção de serem alterados para executar somente unitarios, somente integracao ou ambos, assim como opcoes de debug.

Para executar com as configuracoes padrão do projeto, simplesmente:
```bash
pytest
```

# Estrutura de pastas e projeto

```bash
├── app/ # Estrutura do projeto
│   └── service_bilhetagem/ # Microservico de bilhetagem, conforme desenho de arquitetura
|       ├── alembic/ # Implementacao do database SQLite e migrations para este projeto
|       ├── tests/ # Testes do microservico
|           ├── integration/ # Testes de integracao
|           └── unit/ # Testes de unidade
|       └── src/ # Codigo fonte do projeto
│           ├── adapters/ # Implementacao de interfaces de comunicacao com sistemas e dependencias
|           ├── controllers/ # Implementacao do controlador entre o server (FastAPI) e o core da aplicacao (Usecases)
│           ├── domain/ # Dados do dominio da aplicacao
│           ├── routers/ # Rotas FastAPI
│           ├── services/ # Implementacao de serviços externos, como banco de dados ou integraçõs sistemicas
│           └── usecases/ # Implementacao da regra de negocio da aplicacao
├── docs/ # Documentacoes do projeto
    ├── desenhos/ # Desenho de telas da aplicacao, desenho de arquitetura da infraestrutura e modelagens de banco de dados
    ├── requisitos/ # Detalhamento dos requisitos funcionais e nao funcionais do projeto
└── README.md
```