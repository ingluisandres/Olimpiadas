from pydantic import BaseModel
from typing import Optional


class Athletes(BaseModel):
    _id: Optional[str]
    Name: str
    NOC: str
    Discipline: str

class Coaches(BaseModel):
    _id: Optional[str]
    Name: str
    NOC: str
    Discipline: str
    Event: str

class EntriesGender(BaseModel):
    _id: Optional[str]    
    Discipline: str
    Female: int
    Male: int
    Total: int

class Medals(BaseModel):
    _id: Optional[str]    
    Rank: int
    Team: str
    Gold: int
    Silver: int
    Bronze: int
    Total: int
    RankByTotal: int

class Teams(BaseModel):
    _id: Optional[str]    
    Name: str
    Discipline: str
    NOC: str
    Event: str


class User(BaseModel):
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str
    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    tocken_type: str

class TokenData(BaseModel):
    admin_name: Optional[str] = None    