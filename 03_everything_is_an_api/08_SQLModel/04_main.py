# FastAPI and Pydantic
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlmodel import SQLModel, create_engine, Session, Field, select
from conn_str import conn_str
from typing import Annotated

# HeroBase is a Model with common properties of Hero, HeroCreate, and HeroResponse models
# We will use inheritence to extend HeroBase to Hero, HeroCreate, and HeroResponse models.
# SQLModel is a class that inherits from the SQLModel class and is used to define a model for a database table.
# Field is a class that is used to define a field in a model.


class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    age: int | None = None

# Model to get data from user wthout option of id


class HeroCreate(HeroBase):
    age: int | None = None

# Model to return complete data of hero with id


class HeroResponse(HeroBase):
    id: int
    age: int | None = None

# Model to update data of hero, Here all the fields will be optional so that the user can update any value that needs to be updated


class HeroUpdate(SQLModel):
    name: str | None = None
    secret_name: str | None = None
    age: int | None = None


engine = create_engine(conn_str)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app: FastAPI = FastAPI()

# DB dependency injection


def get_db():
    with Session(engine) as session:
        yield session

# decorator used to define startup events
# startup events: functions that will be called when the FastAPI application starts.


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# get all heros


@app.get("/heroes", response_model=list[Hero])
# Query() used to define min & max values of offset & limit
def get_heros(session: Annotated[Session, Depends(get_db)], offset: int = Query(default=0, le=2), limit: int = Query(default=2, le=4)):
    statement = select(Hero).offset(offset).limit(limit)
    heros = session.exec(statement).all()
    return heros

# post heros


@app.post("/heroes", response_model=HeroResponse)
def create_hero(hero: HeroCreate, db: Annotated[Session, Depends(get_db)]):

    # model_validate() converts hero (hero : HeroCreate) model to Hero so that it can be inserted into DB
    hero_to_insert = Hero.model_validate(hero)

    db.add(hero_to_insert)
    db.commit()
    db.refresh(hero_to_insert)
    return hero_to_insert

# get hero by id


@app.get("/heroes/{hero_id}", response_model=HeroResponse)
def get_hero_by_id(hero_id: int, session: Annotated[Session, Depends(get_db)]):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

# update hero


@app.patch("/heroes/{hero_id}", response_model=HeroResponse)
def update_hero(hero_id: int, hero_data: HeroUpdate, session: Annotated[Session, Depends(get_db)]):
    # get hero
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    print("HERO IN DB", hero)
    print("DATA FROM CLIENT", hero_data)

    # convert hero data into dictionary
    # exclude_unset=True, will exclude any field with None value from the dict
    hero_dict_data = hero_data.model_dump(exclude_unset=True)
    print("DICT HERO DATA", hero_dict_data)

    for key, value in hero_dict_data.items():
        setattr(hero, key, value)

    print("AFTER", hero)

    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

# Delete hero


@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: Annotated[Session, Depends(get_db)]):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"message": "Hero deleted sucessfully"}
