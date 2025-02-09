
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.session import get_db
from app.schemas.camara import CamaraCreate, CamaraResponse
from app.services.camara import CamaraService

router = APIRouter()

# Endpoint para crear una cámara
@router.post(
    "/create",
    response_model= bool,
    status_code=status.HTTP_201_CREATED
)
def create_camara(camara: CamaraCreate, db: Session = Depends(get_db)):
    service = CamaraService(db)
    return service.camara_create(camara)

# Endpoint para obtener una cámara por ID
@router.get(
    "/getbyid/{camara_id}",
    response_model=CamaraResponse,
    status_code=status.HTTP_200_OK
)
def get_camara(camara_id: int, db: Session = Depends(get_db)):
    service = CamaraService(db)
    return service.get_camara_by_id(camara_id)