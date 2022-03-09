from pydantic import BaseModel
from typing import Optional, List


class Serie(BaseModel):
    id: Optional[int] = None
    titulo: List[str] = []
    ano: int
    genero: str
    qtd_temporadas: int

    class Config:
        orm_mode = True

