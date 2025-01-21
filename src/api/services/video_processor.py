import sys
import os
import tempfile
from models.logo_detector import LogoDetector  # Importar desde la carpeta raíz

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../../"))
sys.path.append(project_root)

# Inicializar el detector de logos una vez para optimizar el rendimiento
def initialize_detector():
    """
    Inicializa el detector de logos cargando los pesos y configuraciones necesarias.
    """
    # Ruta base del proyecto
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))

    # Ruta al modelo y data.yaml
    weights_path = os.path.join(project_root, "models", "weights", "best.pt")  # Cambiar según tu estructura
    data_yaml_path = os.path.join(project_root, "data", "dataset_yolo", "data.yaml")

    return LogoDetector(weights_path=weights_path, data_yaml=data_yaml_path)


detector = initialize_detector()  # Cargar el detector al iniciar el módulo


async def process_video(file, thresholds):
    """
    Procesa un video con el detector de logos.
    
    Args:
        file (UploadFile): Archivo subido por el usuario.
        thresholds (dict): Diccionario con los umbrales de confianza por marca.
    
    Returns:
        dict: Estadísticas de detección generadas por el detector.
    """
    # Guardar el archivo subido temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(file.file.read())
        video_path = temp_file.name

    try:
        # Procesar el video con el detector de logos
        stats = detector.process_video(video_path, thresholds)
        return stats
    except Exception as e:
        print(f"Error procesando el video: {str(e)}")
        return {"error": str(e)}
    finally:
        # Limpiar el archivo temporal
        os.remove(video_path)


