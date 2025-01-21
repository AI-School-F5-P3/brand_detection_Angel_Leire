import os
import tempfile
from pathlib import Path

# Importar configuración
from ...config import get_project_root

# Obtener la ruta raíz del proyecto
project_root = get_project_root()

# Ahora podemos importar LogoDetector
from models.logo_detector import LogoDetector

def initialize_detector():
    """
    Inicializa el detector de logos cargando los pesos y configuraciones necesarias.
    """
    weights_path = project_root / "models" / "weights" / "best.pt"
    data_yaml_path = project_root / "data" / "dataset_yolo" / "data.yaml"

    return LogoDetector(weights_path=str(weights_path), data_yaml=str(data_yaml_path))

detector = initialize_detector()

async def process_video(file, thresholds):
    """
    Procesa un video con el detector de logos.
    
    Args:
        file (UploadFile): Archivo subido por el usuario.
        thresholds (dict): Diccionario con los umbrales de confianza por marca.
    
    Returns:
        dict: Estadísticas de detección generadas por el detector.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(file.file.read())
        video_path = temp_file.name

    try:
        stats = detector.process_video(video_path, thresholds)
        return stats
    except Exception as e:
        print(f"Error procesando el video: {str(e)}")
        return {"error": str(e)}
    finally:
        if os.path.exists(video_path):
            os.remove(video_path)