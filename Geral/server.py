from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/saudacao/{nome}")  # Decorator - Rota raíz!
# Async - Será executado de forma assíncrona. Não acontecerá imediatamente.
async def root(nome: str):
    texto = f'Ola {nome}, seja bem vindo!'
    return {"Mensagem": texto}


@app.get("/quadrado/{numero}")
async def quadrado(numero: int):
    quadrado = (numero**2)
    texto = f'O quadrado de {numero} é {quadrado}'

    return {"Mensagem": texto}


@app.get("/dobro")
async def dobro(numero: int):
    dobro = numero*2

    return {"Resultado": f'O dobro de {numero} é {dobro}'}


@app.get("/area-retangulo")
async def arearetangulo(largura: int = 1, altura: int = 1):
    area = largura*altura

    return {"Resultado": f'A area do retangulo com largura {largura} e altura {altura} é {area}'}


class Produto(BaseModel):
    nome: str
    preco: float


@app.post('/produtos')
async def produtos(produto: Produto):
    return {'Mensagem': f'Produto: {produto.nome} - cadastrado com sucesso!'}

@app.get('/produtos')
async def get_produtos(produto):
    return produto.preco