from app.database.conexion import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class CargoModel(Base):
    __tablename__ = 'cargos'
    __table_args__ = {'quote': False}

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    
    # Relación con User
    users = relationship("UserModel", back_populates="cargo")
    
