from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.schemas.schemas import Teams, User
from app.database.database import database, fetch_all, fetch_one, get_current_user


TEAMS = database.Teams

router = APIRouter(
    prefix='/v1/teams',
    tags=['teams']
)


@router.get("/", response_model=List[Teams])
async def get_teams(skip:int=0, limit:int=10, current_user: User = Depends(get_current_user)):
    response = await fetch_all(skip=skip, limit=limit, collection=TEAMS)
    return response

@router.get("/{team}", response_model=Teams)
async def get_team_by_name(name, current_user: User = Depends(get_current_user)):
    response = await fetch_one(name, collection=TEAMS)
    if response:
        return response
    raise HTTPException(404, f"there is no TEAM item with this name:{name}")