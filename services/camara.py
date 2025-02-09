from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.camara import CamaraRepository
from app.schemas.camara import CamaraCreate, CamaraResponse


class CamaraService:
    def __init__(self, db: Session):
        self.camara_repo = CamaraRepository(db)

    def camara_create(self, camara: CamaraCreate):
        # Verificar si la cámara ya existe (por nombre, por ejemplo)
        camara_db = self.camara_repo.get_camara_by_nombre(camara.nombre)
        if camara_db:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="La cámara ya existe"
            )

        # Crear la cámara
        camara_dict = camara.model_dump()
        camara_db = self.camara_repo.create_camara(camara_dict)

        # Retornar la respuesta de la cámara creada
        return True

    def get_camara_by_id(self, camara_id: int):
        camara_db = self.camara_repo.get_camara_by_id(camara_id)
        if not camara_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cámara no encontrada"
            )
        return CamaraResponse(
            id=camara_db.id,
            nombre=camara_db.nombre
        )