from __future__ import annotations
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy import Column, Integer, String


class Serie(Base):
    __tablename__ = 'Serie'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    ano = Column(Integer)
    genero = Column(String)
    qtd_temporadas = Column(Integer)
