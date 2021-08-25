import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

from app.schemas.schemas import Athletes, Coaches, EntriesGender, Medals, Teams
#from app.database.database import fetch_all_todos, fetch_one_todo
from app.database import database


app = FastAPI()

origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/v1/athletes", response_model=List[Athletes])
async def get_athletes(skip:int, limit:int):
    response = await database.fetch_all_athletes(skip=skip, limit=limit)
    return response

@app.get("/v1/athletes/{name}", response_model=Athletes)
async def get_athlete_by_name(name):
    response = await database.fetch_one_athlete(name)
    if response:
        return response
    raise HTTPException(404, f"there is no ATHLETE item with this name:{name}")


@app.get("/v1/coaches", response_model=List[Coaches])
async def get_coaches(skip:int, limit:int):
    response = await database.fetch_all_coaches(skip=skip, limit=limit)
    return response

@app.get("/v1/coaches/{name}", response_model=Coaches)
async def get_coaches_by_name(name):
    response = await database.fetch_one_coach(name)
    if response:
        return response
    raise HTTPException(404, f"there is no COACH item with this name:{name}")


@app.get("/v1/entries-gender", response_model=List[EntriesGender])
async def get_entries_gender(skip:int, limit:int):
    response = await database.fetch_all_entries_gender(skip=skip, limit=limit)
    return response

@app.get("/v1/entries-gender/{discipline}", response_model=EntriesGender)
async def get_entries_gender_by_discipline(discipline):
    response = await database.fetch_one_entries_gender(discipline)
    if response:
        return response
    raise HTTPException(404, f"there is no ENTRIES GENDER item with this discipline:{discipline}")


@app.get("/v1/medals", response_model=List[Medals])
async def get_medals(skip:int, limit:int):
    response = await database.fetch_all_medals(skip=skip, limit=limit)
    return response

@app.get("/v1/medals/{team}", response_model=Medals)
async def get_medals_by_team(team):
    response = await database.fetch_one_medals_by_team(team)
    if response:
        return response
    raise HTTPException(404, f"there is no MEDALS item with this team:{team}")


@app.get("/v1/teams", response_model=List[Teams])
async def get_teams(skip:int, limit:int):
    response = await database.fetch_all_teams(skip=skip, limit=limit)
    return response

@app.get("/v1/teams/{team}", response_model=Teams)
async def get_team_by_name(name):
    response = await database.fetch_one_team(name)
    if response:
        return response
    raise HTTPException(404, f"there is no TEAM item with this name:{name}")