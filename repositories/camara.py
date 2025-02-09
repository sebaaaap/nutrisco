
from typing import Optional
from sqlalchemy.orm import Session
from app.models.camara import CamaraModel

class CamaraRepository:
    
    def __init__(self, db: Session):
        self.db = db
        
    def create_camara(self, data : dict) -> Optional[CamaraModel] : 
        camara_db = CamaraModel(**data) # convierte el dicc altoke a una camaramodel
        
        self.db.add(camara_db)
        self.db.commit()
        self.db.refresh(camara_db)
        
        return camara_db
    
    def get_camara_by_nombre(self, camara_name : str) -> Optional[CamaraModel]:
        return self.db.query(CamaraModel).filter(CamaraModel.nombre == camara_name).first()
    
    def get_camara_by_id(self, camara_id: int):
        return self.db.query(CamaraModel).filter(CamaraModel.id == camara_id).first()