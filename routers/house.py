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

@router.get("/house")
async def get_user():
    result = {"code": 1000, "result": "ok"}
    return JSONResponse(status_code=200, content=jsonable_encoder())
