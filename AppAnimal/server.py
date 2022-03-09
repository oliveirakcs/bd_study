from lib2to3.pytree import Base
from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()


class Animal(BaseModel):
    id: Optional[int]
    nome: str
    idade: int
    sexo: str
    cor: str


banco: List[Animal] = []


@app.get('/animais')
async def listar_animais():
    return banco


@app.get('/animais/{animal_id}')
async def obter_animal(animal_id):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return {'Erro': 'Animal nao localizado'}


@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: str):
    posicao = -1
    # Enumerate retorna o objeto e a pocição dele
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break
    if posicao != -1:
        banco.pop(posicao)
        return{'Mensagem': 'Animal removido com sucesso'}
    else:
        return{'Mensagem': 'Animal nao encontrado'}


@app.post('/animais')
async def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return None
