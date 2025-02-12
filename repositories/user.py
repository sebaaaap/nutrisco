from typing import Optional
from sqlalchemy import *
from sqlalchemy.orm import Session
from app.models.user import UserModel

class UserRepository:

    def __init__(self, db: Session): ## es un constructor
        self.db = db                 ## es como un this de java, se le pasa la session de la bdd

    def user_create(self, userdata: dict):
        user_db = UserModel(**userdata) # desarma el diccionario de una a usermodel
        self.db.add(user_db) # agrega el new user a la bdd
        self.db.commit() # confirma/guarda los cambios 
        self.db.refresh(user_db) # refresca la bdd con el new user
        return user_db
        
    def get_all(self)->Optional[UserModel]:
        # Obtiene todos los usuarios de la base de datos
        return self.db.query(UserModel).all()
    
    def verificar_existencia(self, user_rut: str, user_email: str)->Optional[UserModel]:
        user = self.db.query(UserModel).filter(
        or_(UserModel.user_rut == user_rut, UserModel.user_email == user_email)
        ).first()
        
        return user
    
    def verificar_existencia_rut(self, user_rut: str)->Optional[UserModel]:
        user = self.db.query(UserModel).get(UserModel.user_rut == user_rut).first()
        
        return user
    
    
    
    
    def validar_credenciales(self, user_rut: str, user_password: str) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(and_(UserModel.user_rut == user_rut,
                                                    UserModel.user_password == user_password)).first()
    
    def get_by_nombre(self, user_name: str) -> Optional[UserModel] : 
        return self.db.query(UserModel).filter(UserModel.user_name == user_name).first()