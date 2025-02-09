from app.database.conexion import Base
from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship



class RegistroModel(Base):
    __tablename__ = 'registros'
    __table_args__ = {'quote': False}

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Relación con User
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("UserModel", back_populates="registros")
    
    # Relación con Camara
    camara_id = Column(Integer, ForeignKey('camaras.id'))
    camara = relationship("CamaraModel", back_populates="registros")
    
    # Tiempo de entrada y salida
    tiempo_in = Column(DateTime, nullable=False)
    tiempo_out = Column(DateTime, nullable=True)
    
    # Método para calcular el tiempo dentro de la cámara
    def tiempo_dentro(self):
        if self.tiempo_out:
            return self.tiempo_out - self.tiempo_in
        return None