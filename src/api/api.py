from fastapi import FastAPI, UploadFile, Form
import sqlite3
from models.logo_detector import LogoDetector

app = FastAPI()

# Inicializar detector
detector = LogoDetector(
    weights_path="path/to/best.pt", 
    data_yaml="path/to/data.yaml"
)

@app.post("/process_video/")
async def process_video(file: UploadFile, thresholds: str = Form(...)):
    """Procesa un video subido y retorna estadísticas"""
    conf_thresholds = eval(thresholds)  # Convertir cadena a diccionario
    video_path = f"/tmp/{file.filename}"
    
    with open(video_path, "wb") as f:
        f.write(file.file.read())
    
    # Procesar el video
    stats = detector.process_video(video_path, conf_thresholds)
    
    # Guardar en base de datos (opcional)
    if stats:
        conn = sqlite3.connect("path/to/database.db")
        for brand, data in stats['detections'].items():
            conn.execute(
                "INSERT INTO detections (video_name, brand, timestamp, confidence) VALUES (?, ?, ?, ?)",
                (file.filename, brand, data['timestamp'], data['confidence'])
            )
        conn.commit()
        conn.close()
    
    return stats
