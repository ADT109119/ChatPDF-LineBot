from fastapi import APIRouter, Request, File, Form, UploadFile, Depends, HTTPException
from fastapi.responses import FileResponse

from Model.UploadedFiles import uploadedFiles

from dependencies import verify_line_id

from Service.upload_file import upload_file, delete_file

import os

router = APIRouter(dependencies=[Depends(verify_line_id)])

@router.get("/api/upload")
async def get_all_files_of_this_user(request: Request):
    line_id = request.session.get("line_id")
    list = uploadedFiles.get_all_files_list(line_id)
    response = []
    for i in list:
        response.append({
            "id": i[0],
            "name": i[2],
            "filetype": i[3].split(".")[-1]
        })
    return {"status": "success", "data": response}

@router.get("/api/upload/{id}")
async def get_file_data(request: Request, id: int):
    line_id = request.session.get("line_id")
    list = uploadedFiles.get_all_files_list(line_id)
    response = []
    for i in list:
        response.append({
            "id": i[0],
            "name": i[2],
            "filetype": i[3].split(".")[-1]
        })
    return {"status": "success", "data": response}


@router.post("/api/upload")
async def upload_file_to_server(request: Request, file: UploadFile = File(...)):
    try:
        line_id = request.session.get("line_id")
        # file_id = await uploadedFiles.uploaded_file(line_id, file)
        file_id = await upload_file(line_id, file)
        return {"status": "success", "file_id": file_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# @router.put("/api/upload/{id}")
# async def update_knowledge_base(request: Request, id: int):
#     return FileResponse('public/index.html')

@router.delete("/api/upload/{id}")
async def delete_file_from_server(request: Request, id: int):
    try:
        line_id = request.session.get("line_id")
        delete_file(id, line_id)
    except Exception as e:
        print(e)
        return {"status": "error"}
    return {"status": "success"}

