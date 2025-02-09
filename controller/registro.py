from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.session import get_db
from app.schemas.registro import *
from app.services.registro import RegistroService

router = APIRouter()

@router.post(
    "/ingresar",
    response_model=bool,  # Retornar un booleano
    status_code=status.HTTP_201_CREATED
)
def ingresar_camara(request: Ingresar_Camara_Salir, db: Session = Depends(get_db)):
        service = RegistroService(db)
        return service.ingresar_camara(request.user_rut, request.user_password)


@router.post(
    "/salir",
    response_model=RegistroResponse,  # Retornar el tiempo dentro de la cámara
    status_code=status.HTTP_200_OK
)
def salir_camara(request: Ingresar_Camara_Salir, db: Session = Depends(get_db)):
        service = RegistroService(db)
        return service.salir_camara(request.user_rut, request.user_password)
   