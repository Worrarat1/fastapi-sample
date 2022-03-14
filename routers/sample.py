#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import APIRouter, Query
from fastapi.encoders import jsonable_encoder
from fastapi.param_functions import Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import configparser as conf
import os
from datetime import datetime
from pymongo import MongoClient

# get URL and database
try:
    conf = conf.ConfigParser()
    conf.read('config.ini')
    db_url = conf['DB']['db_url']
    db_name = conf['DB']['db_name']
except KeyError:
    db_url = os.environ['db_url']
    db_name = os.environ['db_name']

# initialize router
router = APIRouter()

# connect to db
conn = MongoClient(db_url)
db = conn[db_name]

# initialize field body
class User(BaseModel):
    first_name: str = Field(..., description="ชื่อจริง") 
    last_name: str = Field(..., description="นามสกุล")
    income: float = Field(0, description="รายได้") 
    
@router.get("/user")
async def get_user():
    coll = db["user"]
    user = coll.find_one(projection={})
    result = {"code": 1000, "result": user}
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.get("/user/{uid}")
async def get_user_one():
    result = {"code": 1000, "result": "ok"}
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.post("/user")
async def insert_user():
    result = {"code": 1000, "result": "ok"}
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
