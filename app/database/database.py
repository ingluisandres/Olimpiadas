import motor.motor_asyncio

from app.schemas.schemas import Athletes, Coaches, EntriesGender, Medals, Teams
from app.security.security import MONGO_INITDB_ROOT_PASSWORD


client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://root:somepassword@localhost:27017") #mongo-db
database = client.olimpiadas

athletes = database.Athletes
coaches = database.Coaches
entries_gender = database.EntriesGender
medals = database.Medals
teams = database.Teams


async def fetch_one_athlete(Name):
    document = await athletes.find_one({"Name":Name})
    return document

async def fetch_all_athletes(skip:int, limit:int):
    todos = []
    cursor = athletes.find().skip(skip).limit(limit)
    async for document in cursor:
        document['_id']=str(document['_id'])
        todos.append(document)
    return todos


async def fetch_one_coach(Name):
    document = await coaches.find_one({"Name":Name})
    return document

async def fetch_all_coaches(skip:int, limit:int):
    todos = []
    cursor = coaches.find().skip(skip).limit(limit)
    async for document in cursor:
        document['_id']=str(document['_id'])
        todos.append(document)
    return todos


async def fetch_one_entries_gender(Discipline):
    document = await entries_gender.find_one({"Discipline":Discipline})
    return document

async def fetch_all_entries_gender(skip:int, limit:int):
    todos = []
    cursor = entries_gender.find().skip(skip).limit(limit)
    async for document in cursor:
        document['_id']=str(document['_id'])
        todos.append(document)
    return todos


async def fetch_one_medals_by_team(Team):
    document = await medals.find_one({"Team":Team})
    return document

async def fetch_all_medals(skip:int, limit:int):
    todos = []
    cursor = medals.find().skip(skip).limit(limit)
    async for document in cursor:
        document['_id']=str(document['_id'])
        todos.append(document)
    return todos


async def fetch_one_team(Name):
    document = await teams.find_one({"Name":Name})
    return document

async def fetch_all_teams(skip:int, limit:int):
    todos = []
    cursor = teams.find().skip(skip).limit(limit)
    async for document in cursor:
        document['_id']=str(document['_id'])
        todos.append(document)
    return todos