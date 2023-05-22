import os
from dotenv import load_dotenv
load_dotenv()

CONTAINER_NAME=os.getenv("CONTAINER_NAME")
ACCESS_KEY=os.getenv("ACCESS_KEY")
IMAGE_NAME=os.getenv("IMAGE_NAME")