from fastapi import APIRouter, Request, Body, Depends
from fastapi.responses import FileResponse, JSONResponse

from Model.KnowledgeBaseFile import knowledgeBaseFile
from pydantic import BaseModel
from Service.embedding import re_embedding

from dependencies import verify_line_id

import os

router = APIRouter(dependencies=[Depends(verify_line_id)])

@router.get("/api/knowledge_base_setting/{id}")
async def get_knowledge_base_file(request: Request, id: int):
    try:
        line_id = request.session.get("line_id")
        list = knowledgeBaseFile.get_all_files(line_id, id)
        response = []
        for i in list:
            response.append({
                "id": i[0],
                "name": i[1],
                "active": i[3],
                "filetype": i[2].split(".")[-1]
            })
        return JSONResponse({"status": "success", "data": response})
    except Exception as e:
        print(e)
        return {"status": "error"}

@router.post("/api/knowledge_base_setting/{id}")
async def add_file_to_knowledge_base(request: Request, id: int, file_id: int = Body(..., embed=True)):
    try:
        line_id = request.session.get("line_id")
        knowledgeBaseFile.add_file_to_knowledge_base(line_id, id, file_id)
        await re_embedding(line_id, id)
        return {"status": "success"}
    except Exception as e:
        print(e)
        return {"status": "error"}

@router.put("/api/knowledge_base_setting/{id}")
async def update_knowledge_base_file(request: Request, id: int, file_id: int = Body(..., embed=True), active: bool = Body(..., embed=True)):
    try:
        line_id = request.session.get("line_id")
        knowledgeBaseFile.setActive(line_id, id, file_id, active)
        await re_embedding(line_id, id)
    except Exception as e:
        print(e)
        return {"status": "error"}
    return {"status": "success"}

@router.delete("/api/knowledge_base_setting/{id}")
async def delete_knowledge_base_file(request: Request, id: int, file_id: int = Body(..., embed=True)):
    try:
        line_id = request.session.get("line_id")
        knowledgeBaseFile.delete_file_from_knowledge_base(id, file_id, line_id)
        await re_embedding(line_id, id)
    except Exception as e:
        print(e)
        return {"status": "error"}
    return {"status": "success"}
