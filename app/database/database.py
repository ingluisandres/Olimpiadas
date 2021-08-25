import motor.motor_asyncio

from app.schemas.schemas import Athletes, Coaches, EntriesGender, Medals, Teams
from app.security.security import MONGO_INITDB_ROOT_PASSWORD


client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://root:somepassword@localhost:27017") #mongo-db
database = client.olimpiadas
athletes = database.Athletes


async def fetch_one_todo(Name):
    document = await athletes.find_one({"Name":Name})
    return document

async def fetch_all_todos(skip:int, limit:int):
    todos = []
    cursor = athletes.find().skip(skip).limit(limit)
    async for document in cursor:
        document['_id']=str(document['_id'])
        todos.append(document)
    return todos

