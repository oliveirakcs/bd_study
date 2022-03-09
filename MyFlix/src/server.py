from telnetlib import SE
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import criar_bd, get_db
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.series import RepositorioSerie

criar_bd()

app = FastAPI()

@app.post('/series')

def criar_serie(serie: schemas.Serie, db: Session = Depends(get_db)):
    serie_criada = RepositorioSerie(db).criar(serie)
    return serie_criada

@app.get('/series')
def listar_serie(db: Session = Depends(get_db)):
    return RepositorioSerie(db).listar()
