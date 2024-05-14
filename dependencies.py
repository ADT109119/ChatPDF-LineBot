from fastapi import Request, HTTPException

async def verify_line_id(request: Request):
    line_id = request.session.get("line_id")
    if not line_id:
        raise HTTPException(status_code=401, detail="line id invalid")
    return True
