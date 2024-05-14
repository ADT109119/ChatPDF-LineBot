from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

from Model.Setting import setting

import os
import requests
import json

router = APIRouter()

@router.get("/liff")
async def get_index():
    return FileResponse('View/dist/index.html')

@router.get("/liff/{path:path}")
async def get_static_files_or_404(path):
    # try open file for path
    file_path = os.path.join("View/dist",path)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    return FileResponse('View/dist/index.html')

# @router.post("/line_id")
# async def session_line_id(request: Request):
#     try:
#         line_id = request.json()["line_id"]
#         request.session["line_id"] = line_id
#         return {"message": "OK"}
#     except:
#         return {"message": "error"}

@router.get("/liffid")
async def get_liffid():
    return {"liff_id": setting.LINE_LIFF_ID}

@router.get("/line_id/{line_id}")
async def session_line_id(request: Request, line_id: str):

    try:
        url = "https://api.line.me/oauth2/v2.1/verify"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "id_token": line_id,
            "client_id": setting.LINE_LOGIN_CHANNEL_ID
        }

        response = requests.post(url, headers=headers, data=data)
        # print(response.sub)
        if response.status_code == 200:
            temp = json.loads(response.text)
            # print(temp)
            request.session["line_id"] = temp['sub']
        else:
            request.session["line_id"] = None

        return {"message": "OK"}
    except:
        return {"message": "error"}
