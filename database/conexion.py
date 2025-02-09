from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a la base de datos PostgreSQL
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/nutrisco"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL)

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()