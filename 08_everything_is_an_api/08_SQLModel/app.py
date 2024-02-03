# SQLModel is wrapper of SQLAlchaemy & Pydantic

from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional
from conn_str import conn_str

# DB Table schema


class Hero(SQLModel, table=True):
    # primary_key will be assigned by DB automatically
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


# Estabish DB connection
    # echo = True will make DB queries in console (intende for the coder) for de-bugging
engine = create_engine(conn_str, echo=True)

# create Tables & DB (call migrations)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# insert data into the table


def create_hero():
    hero1 = Hero(name="M Imran", secret_name="MI")
    hero2 = Hero(name="Rohan Ahmad", secret_name="RA")
    hero3 = Hero(name="Ayra Imran", secret_name="AI")

    with Session(engine) as session:
        session.add(hero1)
        session.add(hero2)
        session.add(hero3)
        session.commit()

# get data from the DB table


def get_hero():
    with Session(engine) as session:
        # statement = select(Hero)
        # statement = select(Hero).limit(2) # selects only specified no of lines
        # statement = select(Hero).offset(2) # skips specified no of lines from the beginning of the table
        statement = select(Hero).where(Hero.id == 1)
        result = session.exec(statement)
        # print(result.all())
        # print(result.first()) # prints first occurance
        # print(result.one())   # prints only one occurance and if there are more than one, it will throw error
        for hero in result:
            print("Individual Hero")
            print(hero.name)

# update the data


def update_hero():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.id == 1)
        # we need to manuplate the data so we get only one entry
        result = session.exec(statement).first()
        print(result)

        result.age = 35
        print(f"Updated data: {result}")

        session.add(result)
        session.commit()

# delete the data


def delete_hero():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.id == 1)
        result = session.exec(statement).first()
        print(result)

        session.delete(result)
        session.commit()

if __name__ == "__main__":
    # create_db_and_tables()
    # create_hero()
    # get_hero()
    # update_hero()
    delete_hero()
