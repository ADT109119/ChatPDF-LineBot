from fastapi import FastAPI, Request, HTTPException, APIRouter
from starlette.middleware.sessions import SessionMiddleware
from Middleware import NoIndexMiddleware

from Controller.line.line import line_router
from Controller.liff import knowledge_base_file, knowledge_base, upload_file, front_end, llm_model

import uvicorn

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="SECRET_KEY")
app.add_middleware(NoIndexMiddleware)

app.include_router(knowledge_base_file.router)
app.include_router(knowledge_base.router)
app.include_router(upload_file.router)
app.include_router(front_end.router)
app.include_router(llm_model.router)
app.include_router(line_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
