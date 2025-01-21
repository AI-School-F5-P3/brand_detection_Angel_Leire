import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import detect  # Importar rutas desde el módulo `api`

# Añadir la raíz del proyecto al PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta de `main.py`
project_root = os.path.abspath(os.path.join(current_dir, "../.."))  # Raíz del proyecto
sys.path.append(project_root)

app = FastAPI(
    title="Logo Detection API",
    description="API para detectar logos en videos",
    version="1.0.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(detect.router, prefix="/api/v1/detect", tags=["detect"])






    




