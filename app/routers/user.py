from fastapi import APIRouter, HTTPException, Depends

from app.schemas.schemas import User
from app.database.database import create_user, get_current_user, get_user


router = APIRouter(
    prefix='/v1/users',
    tags=['users']
)


@router.post('/', response_model=User)
async def create_new_user(user: User, current_user: User = Depends(get_current_user)):
    response = await create_user(user)
    if response:
        return response
    raise HTTPException(400, "Something went wrong") 


@router.get('/', response_model=User)
async def get_user(current_user: User= Depends(get_user)):
    return current_user