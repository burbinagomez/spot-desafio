from azure.storage.blob import BlobServiceClient
import base64
import uuid
from config import ACCESS_KEY,CONTAINER_NAME,IMAGE_NAME
from db import Image

   
def upload_azure_storage(event):
    """
    Este metodo se encarga de subir una imagen a azure storage y no retorna nada
    Parametros:
        - event: dict
            {
            "date": float,
            "camera_id": int,
            "base64_image": str
            }
    
    """
    # Configurar la conexión con Azure Storage
    blob_service_client = BlobServiceClient(account_url=f"https://{IMAGE_NAME}.blob.core.windows.net/",
                                           credential=ACCESS_KEY)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)

    # Decodificar la imagen base64
    imagen_binaria = base64.b64decode(event.base64_image)

    # Subir la imagen a Azure Storage
    blob_client = container_client.get_blob_client(f"{uuid.uuid1()}.jpg")
    blob_client.upload_blob(imagen_binaria, overwrite=True)
    # Guardar la información en la base de datos SQLite
    Image.create(**{
        "date": event.date,
        "camera_id":event.camera_id,
        "image_url": blob_client.url
    })