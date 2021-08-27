from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.schemas.schemas import EntriesGender, User
from app.database.database import database, fetch_all, fetch_one, get_current_user


ENTRIES_GENDER = database.EntriesGender


router = APIRouter(
    prefix='/v1/entries-gender',
    tags=['entries gender']
)


@router.get("/", response_model=List[EntriesGender])
async def get_entries_gender(skip:int=0, limit:int=10, current_user: User = Depends(get_current_user)):
    response = await fetch_all(skip=skip, limit=limit, collection=ENTRIES_GENDER)
    return response

@router.get("/{discipline}", response_model=EntriesGender)
async def get_entries_gender_by_discipline(discipline, current_user: User = Depends(get_current_user)):
    """don't work"""
    response = await fetch_one(discipline, collection=ENTRIES_GENDER)
    if response:
        return response
    raise HTTPException(404, f"there is no ENTRIES GENDER item with this discipline:{discipline}")