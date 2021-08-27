from datetime import timedelta, datetime

import motor.motor_asyncio
from typing import Optional
from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.schemas.schemas import Athletes, Coaches, EntriesGender, Medals, Teams, User, Login, TokenData
from app.security.security import MONGO_INITDB_ROOT_PASSWORD


SECRET_KEY = '260512a9cc0a139082596b89b1c216039748a54ea10f936445ef903afe022fa8'
ALGORITHM = 'HS256'


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='v1/login')

client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://root:somepassword@localhost:27017") # mongo
database = client.olimpiadas

users = database.User


async def fetch_one(Name, 
            collection:motor.motor_asyncio.AsyncIOMotorCollection):
    return await collection.find_one({"Name":Name})

async def fetch_all(skip:int, limit:int, 
            collection:motor.motor_asyncio.AsyncIOMotorCollection):
    """It's not recommendable to query all athletes"""
    cursor = collection.find().skip(skip).limit(limit)
    return [document async for document in cursor]


async def create_user(user):
    document = dict(user)
    #document['_id']=str(document['_id'])
    
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(document['password'])

    document['password']= hashed_password
    result = await users.insert_one(document)
    return document


async def login(email):
    document = await users.find_one({"email":email})
    return document

def verify_password(plain_password, hashed_password):
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    return verify_token(data, credentials_exception)

def verify_token(data:str, credentials_exception):
    try:
        payload = jwt.decode(data, SECRET_KEY, algorithms=[ALGORITHM])
        admin_name: str = payload.get('sub')
        if admin_name is None:
            raise credentials_exception
        token_data = TokenData(admin_name=admin_name)
    except JWTError:
        raise credentials_exception

async def get_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return await users.find_one({"email":payload["sub"]})
    except:
        raise HTTPException(status_code=401, detail="Invalid Email or Password")