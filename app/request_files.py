from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    
    return {"file_size": len(file)}


# @app.post("/upload_file/")
# async def create_upload_file(file: UploadFile):
    
#     return {"filename": file.filename}

@app.post("/upload_file/")
async def create_upload_file(file: Annotated[UploadFile, File()]):
    
    return {"filename": file.filename}