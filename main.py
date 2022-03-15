#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: worrarat
"""

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.cors import CORSMiddleware
from routers import user, house

# initialise Fast APi instance
app = FastAPI(title="FastAPI",
              description="""
     Simple API for demonstration.
     """, version="2.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code,
                        content={"code": 8000,
                                 "description": exc.detail},
                        headers=None)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=400,
                        content={"code": 4000,
                                 "description": str(exc)},
                        headers=None)
    
app.include_router(
    user.router,
    prefix = "/api/v1",
    tags=["User"]
)

app.include_router(
    house.router,
    prefix = "/api/v1",
    tags=["House"]
)

if __name__ == "__main__":
    import os
    os.system("uvicorn main:app --host 0.0.0.0 --port 5000 --reload")
