import os
import sys
from pathlib import Path

# Obtener la ruta absoluta al directorio src
SRC_DIR = Path(__file__).parent.absolute()

# Obtener la ruta absoluta al directorio raíz del proyecto
PROJECT_ROOT = SRC_DIR.parent

# Añadir el directorio raíz al PYTHONPATH si no está ya
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Rutas importantes del proyecto
MODELS_DIR = PROJECT_ROOT / 'models'
DATA_DIR = PROJECT_ROOT / 'data'
WEIGHTS_DIR = MODELS_DIR / 'weights'

# Verificar y crear directorios necesarios
for directory in [MODELS_DIR, DATA_DIR, WEIGHTS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

def get_project_root():
    return PROJECT_ROOT