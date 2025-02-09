from typing import List
from pydantic import BaseModel


from app.schemas.user import UserResponse

class CargoCreate(BaseModel):
    nombre: str

# Esquema para responder con los datos de un Cargo
class CargoResponse(BaseModel):
    id: int
    nombre: str
    users: List[UserResponse] = []        # Lista de usuarios asociados

    class Config:
        from_attributes = True  