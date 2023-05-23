from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
import asyncio
from db import Image, create_tables
from datetime import datetime, timezone
from services import azure

app = FastAPI()

class Event(BaseModel):
    """
    Se especifica los datos que se recibiran en el json de la peticion
    """
    date: float  # Fecha UTC del evento
    base64_image: str  # Imagen en formato base64
    camera_id: int  # ID de la cámara

@app.post("/")
async def post_image(event: Event, background_tasks: BackgroundTasks):
    """
    Se toma el evento recibido por el usuario, y se envia a un proceso interno, donde se sube la imagen a azure y se guarda en base de datos
    """
    try: 

        background_tasks.add_task(azure.upload_azure_storage,event)

        return {"message": "Evento procesado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# if __name__ == "__main__":
create_tables()
