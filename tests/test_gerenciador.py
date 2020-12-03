from core.main import app

from fastapi.testclient import TestClient

def test_quando_listar_carros_deve_ter_como_retorno_codigo_de_status_200():
    cliente = TestClient(app)
    resposta = cliente.get("/veiculos/lista-de-veiculos")
    assert resposta.status_code == 200
    # assert resposta.json() == {"msg": "Hello World"}

def test_quando_listar_carros_formato_de_retorno_deve_ser_json():
    cliente = TestClient(app)
    resposta = cliente.get("/carros")
    assert resposta.headers["Content-Type"] == "application/json"

def test_quando_listar_carros_retorno_deve_ser_uma_lista():
    cliente = TestClient(app)
    resposta = cliente.get("/carros")
    assert isinstance(resposta.json(), list)