from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from db import Image, create_tables
from datetime import datetime, timezone
from services import azure

app = FastAPI()

class Event(BaseModel):
    date: float  # Fecha UTC del evento
    base64_image: str  # Imagen en formato base64
    camera_id: int  # ID de la cámara

@app.post("/")
async def post_image(event: Event):
    try: 

        await azure.save_file_azure_storage(event)

        return {"message": "Evento procesado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# if __name__ == "__main__":
create_tables()
