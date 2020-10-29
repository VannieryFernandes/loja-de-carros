from fastapi import FastAPI

app = FastAPI()


@app.get("/carros")
async def lista_carros():
    return []
