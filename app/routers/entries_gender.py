from fastapi import APIRouter
from typing import List

from app.schemas.schemas import EntriesGender
from app.database.database import fetch_all_entries_gender, fetch_one_entries_gender


router = APIRouter(
    prefix='/v1/entries-gender',
    tags=['entries gender']
)


@router.get("/", response_model=List[EntriesGender])
async def get_entries_gender(skip:int=0, limit:int=10):
    response = await fetch_all_entries_gender(skip=skip, limit=limit)
    return response

@router.get("/{discipline}", response_model=EntriesGender)
async def get_entries_gender_by_discipline(discipline):
    response = await fetch_one_entries_gender(discipline)
    if response:
        return response
    raise HTTPException(404, f"there is no ENTRIES GENDER item with this discipline:{discipline}")