import os
import sys
from pathlib import Path

def setup_project_paths():
    """
    Configura las rutas del proyecto y añade el directorio raíz al PYTHONPATH
    
    Returns:
        Path: Ruta raíz del proyecto
    """
    # Obtener la ruta al directorio actual
    current_file = Path(__file__).resolve()
    
    # Obtener la ruta raíz del proyecto (2 niveles arriba de src/config)
    project_root = current_file.parent.parent.parent
    
    # Añadir la raíz del proyecto al PYTHONPATH si no está ya
    project_root_str = str(project_root)
    if project_root_str not in sys.path:
        sys.path.insert(0, project_root_str)
    
    return project_root