from app.database.conexion import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import *

class UserModel(Base):
    __tablename__ = 'users'
    __table_args__ = {'quote': False}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    user_lastname = Column(String, nullable=False)
    user_rut = Column(String, nullable=False, unique=True)
    user_email = Column(String, nullable=False, unique=True)
    user_password = Column(String, nullable=False)
    
    # Relación con Camara
    id_camara = Column(Integer, ForeignKey('camaras.id'))
    camara = relationship("CamaraModel", back_populates="users")
    
    # Relación con Cargo
    id_cargo = Column(Integer, ForeignKey('cargos.id'))
    cargo = relationship("CargoModel", back_populates="users")
    
    # Relación con Registro
    registros = relationship("RegistroModel", back_populates="user")
    


    