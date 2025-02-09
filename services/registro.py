from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.registro import RegistroRepository
from app.repositories.user import UserRepository
from app.schemas.registro import RegistroCreate, RegistroResponse
from app.models.registro import RegistroModel
from datetime import datetime

class RegistroService:
    def __init__(self, db: Session):
        self.registro_repo = RegistroRepository(db)
        self.user_repo = UserRepository(db)

    def ingresar_camara(self, user_rut: str, user_password: str):
        try:
            # Verificar las credenciales del usuario
            user_db = self.user_repo.validar_credenciales(user_rut, user_password)
            if not user_db:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Credenciales inválidas"
                )

            # Crear el registro de entrada
            registro_data = {
                "user_id": user_db.id,
                "camara_id": user_db.id_camara,  # Asumimos que el usuario tiene una cámara asignada
                "tiempo_in": datetime.now()
            }
            self.registro_repo.create_registro(registro_data)

            # Retornar True si el registro se crea correctamente
            return True

        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al registrar la entrada: {str(e)}"
            )

    
    def salir_camara(self, user_rut: str, user_password: str):
        try:
            # Verificar las credenciales del usuario
            user_db = self.user_repo.validar_credenciales(user_rut, user_password)
            if not user_db:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Credenciales inválidas"
                )

            # Obtener el último registro de entrada del usuario
            registro_db = self.registro_repo.get_ultimo_registro(user_db.id)
            if not registro_db or registro_db.tiempo_out:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="no hay registro de entrada"
                )

            # Actualizar el tiempo de salida
            tiempo_out = datetime.now()
            self.registro_repo.actualizar_salida(registro_db.id, tiempo_out)

            # Calcular el tiempo dentro de la cámara
            tiempo_dentro = registro_db.tiempo_dentro()

            # Retornar la información en el formato esperado
            return {
                "id": registro_db.id,
                "user_id": registro_db.user_id,
                "camara_id": registro_db.camara_id,
                "tiempo_in": registro_db.tiempo_in,
                "tiempo_out": tiempo_out,
                "tiempo_dentro": str(tiempo_dentro)  # Convertir a cadena
            }

        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al registrar la salida: {str(e)}"
            )