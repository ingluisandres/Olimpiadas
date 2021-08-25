from pydantic import BaseModel
from typing import Optional


class Athletes(BaseModel):
    _id: Optional[str]
    Name: str
    NOC: str
    Discipline: str

class Coaches(BaseModel):
    name: str
    noc: str
    discipline: str
    event: str

class EntriesGender(BaseModel):
    discipline: str
    female: int
    male: int
    total: int

class Medals(BaseModel):
    rank: int
    team: str
    gold: str
    silver: str
    bronze: str
    total: str
    rankbytotal: str

class Teams(BaseModel):
    name: str
    discipline: str
    noc: str
    event: str