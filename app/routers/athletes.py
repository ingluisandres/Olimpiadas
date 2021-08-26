from fastapi import APIRouter, Depends
from typing import List

from app.schemas.schemas import Athletes, User
from app.database.database import fetch_all_athletes, fetch_one_athlete, get_current_user


router = APIRouter(
    prefix='/v1/athletes',
    tags=['athletes']
)


@router.get("/", response_model=List[Athletes])
async def get_athletes(skip:int=0, limit:int=10, current_user: User = Depends(get_current_user)):
    response = await fetch_all_athletes(skip=skip, limit=limit)
    return response

@router.get("/{name}", response_model=Athletes)
async def get_athlete_by_name(name, current_user: User = Depends(get_current_user)):
    response = await fetch_one_athlete(name)
    if response:
        return response
    raise HTTPException(404, f"there is no ATHLETE item with this name:{name}")