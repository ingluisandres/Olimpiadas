from fastapi import APIRouter, Depends
from typing import List

from app.schemas.schemas import Coaches, User
from app.database.database import fetch_all_coaches, fetch_one_coach, get_current_user


router = APIRouter(
    prefix='/v1/coaches',
    tags=['coaches']
)


@router.get("/", response_model=List[Coaches])
async def get_coaches(skip:int=0, limit:int=10, current_user: User = Depends(get_current_user)):
    response = await fetch_all_coaches(skip=skip, limit=limit)
    return response

@router.get("/{name}", response_model=Coaches)
async def get_coaches_by_name(name, current_user: User = Depends(get_current_user)):
    response = await fetch_one_coach(name)
    if response:
        return response
    raise HTTPException(404, f"there is no COACH item with this name:{name}")
