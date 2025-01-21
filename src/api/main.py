from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar configuración primero
from ..config import get_project_root

# Obtener la ruta raíz del proyecto
get_project_root()

# Ahora importar las rutas
from .routes import detect

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