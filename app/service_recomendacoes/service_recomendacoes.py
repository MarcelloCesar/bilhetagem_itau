from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def service_recomendacoes():
    return {
        "recomendacoes": [
            {
                "id": "1",
                "nome": "Pipoca"
            },
            {
                "id": "2",
                "nome": "Ingresso VIP"
            },
            {
                "id": "3",
                "nome": "Bebida refrigerante"
            }
        ]
    }
