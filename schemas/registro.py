from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# Esquema para crear un Registro
class RegistroCreate(BaseModel):
    user_id: int      # Clave foránea a User
    camara_id: int    # Clave foránea a Camara
    tiempo_in: datetime  # Tiempo de entrada


class Ingresar_Camara_Salir(BaseModel):
    user_rut: str
    user_password: str
    
class RegistroResponse(BaseModel):
    id: int
    user_id: int
    camara_id: int
    tiempo_in: datetime
    tiempo_out: datetime
    tiempo_dentro: str


    class Config:
        from_attributes = True  # Permite crear instancias desde objetos ORM