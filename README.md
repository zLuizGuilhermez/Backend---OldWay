# FastAPI + SQLite - Projeto Base

Projeto backend em Python com FastAPI e SQLite, pronto para desenvolvimento e handoff para equipe.

## Objetivo

Este projeto entrega:
- Estrutura organizada por camadas.
- CRUD exemplo para recurso `items`.
- Persistencia em SQLite com SQLAlchemy.
- Documentacao tecnica para onboard rapido.

## Stack

- Python 3.10+
- FastAPI
- SQLAlchemy 2.x
- SQLite
- Uvicorn

## Estrutura de pastas

```text
.
├── app
│   ├── core
│   │   └── config.py
│   ├── db
│   │   ├── models
│   │   │   └── item_model.py
│   │   ├── repositories
│   │   │   └── item_repository.py
│   │   ├── base.py
│   │   └── session.py
│   ├── fastapi
│   │   ├── controllers
│   │   │   ├── health_controller.py
│   │   │   └── item_controller.py
│   │   ├── schemas
│   │   │   └── item_schema.py
│   │   └── router.py
│   ├── main.py
│   └── services
│       └── item_service.py
├── docs
│   ├── handoff.md
│   └── organizacao_pastas.txt
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Como executar localmente

1. Criar ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. (Opcional) Configurar variaveis de ambiente:

```bash
cp .env.example .env
```

4. Subir aplicacao:

```bash
uvicorn app.main:app --reload
```

API disponivel em `http://127.0.0.1:8000`.

## Documentacao da API

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints principais

- `GET /health`
- `POST /api/v1/items/`
- `GET /api/v1/items/`
- `GET /api/v1/items/{item_id}`
- `PUT /api/v1/items/{item_id}`
- `DELETE /api/v1/items/{item_id}`

## Banco de dados

- Banco padrao: `app.db` na raiz do projeto.
- URL configuravel por `DATABASE_URL`.
- Tabelas criadas automaticamente no startup.

## Handoff para equipe

A documentacao completa para passagem esta em:

- `docs/handoff.md`
- `docs/organizacao_pastas.txt`

Este arquivo inclui arquitetura, fluxo de requisicao, orientacoes de deploy e backlog tecnico recomendado.
