from fastapi import APIRouter, Depends
from typing import List

from app.schemas.schemas import Teams, User
from app.database.database import fetch_all_teams, fetch_one_team, get_current_user


router = APIRouter(
    prefix='/v1/teams',
    tags=['teams']
)


@router.get("/", response_model=List[Teams])
async def get_teams(skip:int=0, limit:int=10, current_user: User = Depends(get_current_user)):
    response = await fetch_all_teams(skip=skip, limit=limit)
    return response

@router.get("/{team}", response_model=Teams)
async def get_team_by_name(name, current_user: User = Depends(get_current_user)):
    response = await fetch_one_team(name)
    if response:
        return response
    raise HTTPException(404, f"there is no TEAM item with this name:{name}")