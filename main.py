import shutil
from fastapi import FastAPI,UploadFile,File
import cv2


app = FastAPI()

@app.post('/')
async def root(file: UploadFile = File(...),q: str = None):
    path = file.filename
    img = cv2.imread(path)
    q=img.shape

    return {"file_name": file.filename,"q": q}
