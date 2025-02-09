from fastapi import FastAPI
from app.database.conexion import Base, engine
from app.controller.user import router as user_router
from app.controller.camara import router as camara_router
from app.controller.cargo import router as cargo_router
from app.controller.registro import router as registro_router

from app.models import (
    CamaraModel,
    CargoModel,
    UserModel,
    RegistroModel
)


app = FastAPI()

# Crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)
@app.get("/")
def read_root():
    return {"chupalo"}
# Monta las rutas
app.include_router(user_router, prefix="/adecco/users")
app.include_router(camara_router, prefix="/adecco/camara")
app.include_router(registro_router, prefix="/adecco/registro")
app.include_router(cargo_router, prefix="/adecco/cargo")
