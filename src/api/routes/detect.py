from fastapi import APIRouter, UploadFile, File
from ..services.video_processor import process_video

router = APIRouter()

@router.post("/video")
async def detect_logos_in_video(
    file: UploadFile = File(...),
    confidence_threshold: float = 0.5
):
    thresholds = {
        'adidas': confidence_threshold,
        'nike': confidence_threshold,
        'puma': confidence_threshold
    }
    
    results = await process_video(file, thresholds)
    return results