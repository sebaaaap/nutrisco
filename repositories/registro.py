from typing import Optional
from sqlalchemy.orm import Session
from app.models.registro import RegistroModel
from datetime import datetime
class RegistroRepository: 
    
    def __init__(self, db : Session):
        self.db = db
    
    def create_registro(self, data_registro : dict) -> Optional[RegistroModel]:
        register_db = RegistroModel(**data_registro)
        
        self.db.add(register_db)
        self.db.commit()
        self.db.refresh(register_db)
        
        return register_db   
    
    def get_ultimo_registro(self, user_id: int) -> Optional[RegistroModel]:
        return self.db.query(RegistroModel).filter(
            RegistroModel.user_id == user_id,
            RegistroModel.tiempo_out.is_(None)  # Solo registros sin hora de salida
        ).order_by(RegistroModel.tiempo_in.desc()).first()

    def actualizar_salida(self, registro_id: int, tiempo_out: datetime) -> Optional[RegistroModel]:
        registro_db = self.db.query(RegistroModel).filter(RegistroModel.id == registro_id).first()
        if registro_db:
            registro_db.tiempo_out = tiempo_out
            self.db.commit()
            self.db.refresh(registro_db)
        return registro_db 