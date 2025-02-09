from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.cargo import CargoRepository
from app.schemas.cargo import CargoCreate, CargoResponse
from app.models.cargo import CargoModel

class CargoService:
    def __init__(self, db: Session):
        self.cargo_repo = CargoRepository(db)

    def cargo_create(self, cargo: CargoCreate):
        # Verificar si el cargo ya existe (por nombre, por ejemplo)
        cargo_db = self.cargo_repo.get_cargo_by_nombre(cargo.nombre)
        if cargo_db:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="El cargo ya existe"
            )

        # Crear el cargo
        cargo_dict = cargo.model_dump()
        cargo_db = self.cargo_repo.create_cargo(cargo_dict)

        # Retornar la respuesta del cargo creado
        return True

    def get_cargo_by_id(self, cargo_id: int):
        cargo_db = self.cargo_repo.get_cargo_by_id(cargo_id)
        if not cargo_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cargo no encontrado"
            )
        return CargoResponse(
            id=cargo_db.id,
            nombre=cargo_db.nombre
        )
        