
from typing import Optional
from sqlalchemy.orm import *
from app.models.cargo import CargoModel
class CargoRepository : 
    def __init__(self, db: Session):
        self.db = db
        
    def create_cargo(self, data_cargo: dict) -> Optional[CargoModel]:
        cargo_db = CargoModel(**data_cargo)
        
        self.db.add(cargo_db)
        self.db.commit()
        self.db.refresh(cargo_db)
        
        return cargo_db
    
    def get_cargo_by_nombre(self, cargo_name : str) -> Optional[CargoModel]:
        return self.db.query(CargoModel).filter(CargoModel.nombre == cargo_name).first()
    
    def get_cargo_by_id(self, cargo_id: int):
        return self.db.query(CargoModel).filter(CargoModel.id == cargo_id).first()
