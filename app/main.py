import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from app.schemas.schemas import Athletes, Coaches, EntriesGender, Medals, Teams
from app.database.database import fetch_all_todos, fetch_one_todo


app = FastAPI()

origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/v1/athlete", response_model=List[Athletes])
async def get_athletes(skip:int, limit:int):
    response = await fetch_all_todos(skip=skip, limit=limit)
    return response

@app.get("/v1/athlete/{name}", response_model=Athletes)
async def get_athletes_by_name(name):
    response = await fetch_one_todo(name)
    if response:
        return response
    raise HTTPException(404, f"there is no ATHLETE item with this {name}")
