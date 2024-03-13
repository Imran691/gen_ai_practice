from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import SQLModel, Field
from conn_str import conn_str

class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str

class Team(TeamBase, table=True):
    id: int = Field(default=None, primary_key=True)

class TeamCreate(TeamBase):
    pass

class TeamResponse(TeamBase):
    id: int

class TeamUpdate(SQLModel):
    name: str | None = None
    headquarters: str | None = None
    
class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str

class Hero(HeroBase, table=True):
    id: int = Field(default=None, primary_key=True)
    age: int | None = None

class HeroCreate(HeroBase):
    age: int | None = None

class HeroResponse(HeroBase):
    id: int
    age: int | None = None

class HeroUpdate(SQLModel):
    name: str | None = None
    secret_name: str | None = None
    age: int | None = None

