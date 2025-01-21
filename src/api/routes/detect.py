from fastapi import APIRouter, UploadFile, Form
from ..services.video_processor import process_video  # Import desde `services`

router = APIRouter()

@router.post("/video")
async def detect_from_video(file: UploadFile, thresholds: str = Form(...)):
    """
    Procesa un video subido y retorna estadísticas de detección de logos.
    """
    thresholds_dict = eval(thresholds)  # Convertir string a diccionario
    stats = await process_video(file, thresholds_dict)
    return stats
