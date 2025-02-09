from pydantic import BaseModel, EmailStr

# Esquema para crear un User
class UserCreate(BaseModel):
    user_name: str
    user_lastname: str
    user_rut: str
    user_email: EmailStr
    user_password: str
    id_camara: int  # Clave foránea a Camara
    id_cargo: int   # Clave foránea a Cargo

# Esquema para responder con los datos de un User
class UserResponse(BaseModel):
    id: int
    user_name: str
    user_lastname: str
    user_rut: str
    user_email: EmailStr
    id_camara: int
    id_cargo: int

    class Config:
        from_attributes = True 

class MessageResponse(BaseModel):
    message: str

    # Configuración para Pydantic V2
    model_config = {
        "from_attributes": True  # Permite crear instancias desde objetos ORM
    }