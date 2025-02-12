from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.user import UserRepository
from app.repositories.camara import CamaraRepository 
from app.repositories.cargo import CargoRepository
from app.repositories.registro import  RegistroRepository
from app.schemas.user import UserCreate, UserResponse
from datetime import datetime
from app.models.user import UserModel

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
    
    def users_get_all(self) -> List[UserResponse]:
        try:
            usuarios = self.user_repo.get_all()
            
            
            # Convertir los objetos SQLAlchemy a modelos Pydantic
            usuarios_response = [
                UserResponse(
                    id=usuario.id,
                    user_name=usuario.user_name,
                    user_lastname=usuario.user_lastname,
                    user_rut=usuario.user_rut,
                    user_email=usuario.user_email,  # Coma agregada aquí
                    id_camara=usuario.id_camara,   # Asegúrate de que este campo exista
                    id_cargo=usuario.id_cargo       # Asegúrate de que este campo exista
                )
                for usuario in usuarios
            ]
            
            return usuarios_response
        
        except HTTPException as http_exc:
            # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc

        except Exception as e:
            # Manejar cualquier error inesperado
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al obtener los usuarios: {str(e)}"
            )

    def get_by_nombre(self, user_name: str) -> Optional[UserModel]:
     try:
        # Obtener el usuario desde el repositorio
        usuario = self.user_repo.get_by_nombre(user_name)
        
        # Verificar si el usuario existe
        if usuario is None:
            return None
        
        # Convertir el objeto SQLAlchemy a un modelo Pydantic
        return UserModel(**usuario.to_dict())# Opción 1: Usar **usuario.__dict__
        
     except HTTPException as http_exc:
        # Re-lanzar la excepción HTTPException para que FastAPI la maneje
        raise http_exc    
        
     except Exception as e:
        # Manejar cualquier error inesperado
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener el usuario: {str(e)}"
        )