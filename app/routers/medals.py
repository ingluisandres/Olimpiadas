from fastapi import APIRouter, Depends
from typing import List

from app.schemas.schemas import Medals, User
from app.database.database import fetch_all_medals, fetch_one_medals_by_team, get_current_user


router = APIRouter(
    prefix='/v1/medals',
    tags=['medals']
)


@router.get("/", response_model=List[Medals])
async def get_medals(skip:int=0, limit:int=10, current_user: User = Depends(get_current_user)):
    response = await fetch_all_medals(skip=skip, limit=limit)
    return response

@router.get("/{team}", response_model=Medals)
async def get_medals_by_team(team, current_user: User = Depends(get_current_user)):
    response = await fetch_one_medals_by_team(team)
    if response:
        return response
    raise HTTPException(404, f"there is no MEDALS item with this team:{team}")