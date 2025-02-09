from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.session import get_db
from app.schemas.cargo import CargoCreate, CargoResponse
from app.services.cargo import CargoService

router = APIRouter()

# Endpoint para crear un cargo
@router.post(
    "/create",
    response_model= bool,
    status_code=status.HTTP_201_CREATED
)
def create_cargo(cargo: CargoCreate, db: Session = Depends(get_db)):
    service = CargoService(db)
    return service.cargo_create(cargo)

# Endpoint para obtener un cargo por ID
@router.get(
    "/getbyid/{cargo_id}",
    response_model=CargoResponse,
    status_code=status.HTTP_200_OK
)
def get_cargo(cargo_id: int, db: Session = Depends(get_db)):
    service = CargoService(db)
    return service.get_cargo_by_id(cargo_id)