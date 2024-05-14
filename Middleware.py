from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

class NoIndexMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Robots-Tag"] = "noindex"
        return response
