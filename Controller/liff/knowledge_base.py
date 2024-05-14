from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import FileResponse, JSONResponse

from Model.KnowledgeBase import knowledgeBase

from pydantic import BaseModel
from dependencies import verify_line_id

import os

router = APIRouter(dependencies=[Depends(verify_line_id)])

@router.get("/api/knowledge_base")
async def get_knowledge_base(request: Request):
    try:
        line_id = request.session.get("line_id")
        list = knowledgeBase.get_list(line_id)
        response = []
        for i in list:
            response.append({
                "id": i[0],
                "name": i[2],
                "model": i[3],
                "temperature": i[4],
                "score_threshold": i[5],
                "search_item_limit": i[6],
            })
        return JSONResponse({"status":"success","data":response})
    except Exception as e:
        print(e)
        return {"status": "error"}

@router.get("/api/knowledge_base/{id}")
async def get_knowledge_base_setting(request: Request, id: int):
    try:
        line_id = request.session.get("line_id")
        response = knowledgeBase.get_setting(id, line_id)
        response = {
            "id": response['id'],
            "name": response['name'],
            "model": response['model'],
            "temperature": response['temperature'],
            "score_threshold": response['score_threshold'],
            "search_item_limit": response['search_item_limit'],
        }
        return JSONResponse({"status":"success","data":response})
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="unable to access")

class CreateKnowledgeBaseData(BaseModel):
    name: str
    model: int
    temperature: float
    score_threshold: float
    search_item_limit: int

@router.post("/api/knowledge_base")
async def create_knowledge_base(request: Request, postdata: CreateKnowledgeBaseData):
    try:
        line_id = request.session.get("line_id")
        data = postdata.dict()
        temperature = 1 if abs(data['temperature']) > 1 else abs(data['temperature'])
        score_threshold = 1 if abs(data['score_threshold']) > 1 else abs(data['score_threshold'])
        search_item_limit = 1 if abs(data['search_item_limit']) < 1 else abs(data['search_item_limit'])

        knowledgeBase.saveData((None, line_id, data['name'], int(data['model']), temperature, score_threshold, search_item_limit, ))
        return {"status": "success"}
    except Exception as e:
        print(e)
        return {"status": "error"}

class KnowledgeBaseData(BaseModel):
    id: int
    name: str
    model: int
    temperature: float
    score_threshold: float
    search_item_limit: int

@router.put("/api/knowledge_base/{id}")
async def update_knowledge_base(request: Request, id: int, postdata: KnowledgeBaseData):
    line_id = request.session.get("line_id")
    data = postdata.dict()
    data['temperature'] = 1 if abs(data['temperature']) > 1 else abs(data['temperature'])
    data['score_threshold'] = 1 if abs(data['score_threshold']) > 1 else abs(data['score_threshold'])
    data['search_item_limit'] = 1 if abs(data['search_item_limit']) < 1 else abs(data['search_item_limit'])
    try:
        knowledgeBase.updateData(id, line_id, data)
    except Exception as e:
        print(e)
        return {"status": "error"}
    return {"status": "success"}

@router.delete("/api/knowledge_base/{id}")
async def delete_knowledge_base(request: Request, id: int):
    line_id = request.session.get("line_id")
    try:
        knowledgeBase.deleteData(id, line_id)
    except Exception as e:
        print(e)
        return {"status": "error"}
    return {"status": "success"}

