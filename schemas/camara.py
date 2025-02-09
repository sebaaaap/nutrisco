from typing import List
from pydantic import BaseModel

from app.schemas.user import UserResponse

class CamaraCreate(BaseModel):
    nombre: str

# Esquema para responder con los datos de una Camara
class CamaraResponse(BaseModel):
    id: int
    nombre: str
    users: List[UserResponse] = []  # Lista de usuarios asociados

    class Config:
        from_attributes = True 