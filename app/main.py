import sys
sys.path.append("..")

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.routers import athletes, coaches, entries_gender, medals, teams


app = FastAPI()

origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(athletes.router)
app.include_router(coaches.router)
app.include_router(entries_gender.router)
app.include_router(medals.router)
app.include_router(teams.router)