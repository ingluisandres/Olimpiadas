from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.schemas.schemas import Medals, User
from app.database.database import database, fetch_all, fetch_one, get_current_user


MEDALS = database.Medals


router = APIRouter(
    prefix='/v1/medals',
    tags=['medals']
)


@router.get("/", response_model=List[Medals])
async def get_medals(skip:int=0, limit:int=10, current_user: User = Depends(get_current_user)):
    response = await fetch_all(skip=skip, limit=limit, collection=MEDALS)
    return response

@router.get("/{team}", response_model=Medals)
async def get_medals_by_team(team, current_user: User = Depends(get_current_user)):
    """don't work"""
    response = await fetch_one(team, collection=MEDALS)
    if response:
        return response
    raise HTTPException(404, f"there is no MEDALS item with this team:{team}")