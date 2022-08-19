from fastapi import FastAPI
from pydantic import BaseModel


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False


app = FastAPI()

produtos = [
    Produto(id=1, nome='Playstation 5', preco=5745.55, em_oferta=True),
    Produto(id=2, nome='Nintendo Wii', preco=2245.12),
    Produto(id=3, nome='X-BOX 360', preco=1523.89, em_oferta=True),
    Produto(id=4, nome='Super Nintendo', preco=225),
    Produto(id=5, nome='Atari', preco=199, em_oferta=True)
]


@app.get('/')
async def index():
    return {'Geek': 'Universityr'}


@app.get('/produtos/{id}')
async def buscar_produto(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
    return None


@app.put('/produtos/{id}')
async def atualizar_produto(id: int, produto: Produto):
    for prod in produtos:
        if prod.id == id:
            prod = produto
            return prod
    return None
