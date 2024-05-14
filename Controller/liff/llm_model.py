from fastapi import APIRouter, Request, Body
from fastapi.responses import FileResponse

from Model.Setting import setting

import os

router = APIRouter()

@router.get("/api/model")
async def get_all_llm_models(request: Request):
    try:
        line_id = request.session.get("line_id")
        list = setting.MODEL_NAME
        response = []
        for i, item in enumerate(list):
            response.append({
                "id": i,
                "name": item,
            })
        return {"status": "success", "data": response}
    except Exception as e:
        print(e)
        return {"status": "error"}
