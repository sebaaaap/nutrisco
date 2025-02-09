from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.user import UserRepository
from app.repositories.camara import CamaraRepository 
from app.repositories.cargo import CargoRepository
from app.repositories.registro import  RegistroRepository
from app.schemas.user import UserCreate, UserResponse
from datetime import datetime

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)
        self.camara_repo = CamaraRepository(db)
        self.cargo_repo = CargoRepository(db)
        self.registro_repo = RegistroRepository(db)

    def user_create(self, user: UserCreate):
        try:
            # Verificar si el usuario ya existe
            if self.user_repo.verificar_existencia(user.user_rut, user.user_email):
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="El usuario ya existe"
                )

            # Crear el usuario
            user_dict = user.model_dump()  # Convertir el esquema Pydantic a un diccionario
            user_db = self.user_repo.user_create(user_dict)

            # Retornar True si el usuario se crea correctamente
            return True

        except HTTPException as http_exc:
            # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc

        except Exception as e:
            # Manejar cualquier otro error inesperado
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al crear el usuario: {str(e)}"
            )
            
        
        
