from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.database import database


ACCESS_TOKEN_EXPIRE_MINUTES = 30


router = APIRouter(
    prefix='/v1/login',
    tags=['login']
)


@router.post('/')
async def login(user: OAuth2PasswordRequestForm=Depends()):
    user_admin = await database.login(email=user.username)
    if not user_admin:
        raise HTTPException(
            status_code=404, detail='Invalid Credentials'
        )
    if not database.verify_password(user.password, user_admin["password"]):
        raise HTTPException(
            status_code=404, detail='Incorrect admin name or password'
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # constant
    access_token = database.create_access_token(
        data={'sub': user_admin["email"]}, expires_delta=access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}