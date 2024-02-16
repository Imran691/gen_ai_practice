from sqlmodel import SQLModel, create_engine, Session, select, Field
from typing import Optional
from conn_str import conn_str

engine = create_engine(conn_str, echo=True)

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    country: str

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_teams_and_heros():
    with Session(engine) as session:
        team_1 = Team(name="Avengers", country="USA")
        team_2 = Team(name="X-Men", country="USA")
        session.add_all([team_1, team_2])
        session.commit()

        hero_1 = Hero(name="Spider-Man", secret_name="Peter Parker", team_id=team_2.id)
        hero_2 = Hero(name="Iron Man", secret_name="Tony Stark", team_id=team_1.id)
        session.add_all([hero_1, hero_2])
        session.commit()

def get_hero_by_where():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.id == 1)
        hero = session.exec(statement).first()
        print(hero.name)

def get_hero_by_join():
    with Session(engine) as session:
        statement = select(Team).join(Hero)
        result = session.exec(statement)
        for hero in result:
            print(hero.name, hero.country)

def update_team():
    with Session(engine) as session:
        statement = select(Team).where(Team.id == 1)
        team = session.exec(statement).first()
        # print(team.name)
        team.country = "Canada"
        session.add(team)
        session.commit()

def main():
    # create_db_and_tables()
    # create_teams_and_heros()
    # get_hero_by_where()
    get_hero_by_join()
    # update_team()
    

if __name__ == "__main__":
    main()