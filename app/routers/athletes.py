from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.schemas.schemas import Athletes, User
from app.database.database import database, fetch_all, fetch_one, get_current_user


ATHLETES = database.Athletes


router = APIRouter(
    prefix='/v1/athletes',
    tags=['athletes']
)


@router.get("/", response_model=List[Athletes])
async def get_athletes(skip:int=0, limit:int=10, current_user: User = Depends(get_current_user)):
    response = await fetch_all(skip=skip, limit=limit, collection=ATHLETES)
    return response

@router.get("/{Name}", response_model=Athletes)
async def get_athlete_by_name(Name, current_user: User = Depends(get_current_user)):
    response = await fetch_one({"Name":Name}, collection=ATHLETES)
    if response:
        return response
    raise HTTPException(404, f"there is no ATHLETE item with this name:{Name}")