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
    # the team in "team.id" is the table in DB, not the Team schema in this code
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_teams_and_heros():
    with Session(engine) as session:
        # team_1 = Team(name="Avengers", country="USA")
        # team_2 = Team(name="X-Men", country="USA")
        # session.add_all([team_1, team_2])
        # session.commit()

        # hero_1 = Hero(name="Spider-Man", secret_name="Peter Parker", team_id=team_2.id)
        # hero_2 = Hero(name="Iron Man", secret_name="Tony Stark", team_id=team_1.id)
        # session.add_all([hero_1, hero_2])
        hero_3 = Hero(name="Super-Man", secret_name="Clark Kent")
        session.add(hero_3)
        session.commit()

def get_hero_by_where():
    with Session(engine) as session:
        statement = select(Hero, Team).where(Hero.team_id == Team.id)
        results = session.exec(statement)
        for hero, team in results:
            print("Hero:", hero.name, "Team:", team.name)

# Read connected data
def get_hero_by_join():
    with Session(engine) as session:
        statement = select(Hero, Team).join(Team)
        result = session.exec(statement)
        for hero, team in result:
            print("Hero: ", hero.name, "Team: ", team.name)

def get_hero_by_left_join():
    with Session(engine) as session:
        statement = select(Hero, Team).join(Team, isouter=True)
        result = session.exec(statement)
        for hero, team in result:
            print("Hero: ", hero.name, "Team: ", team.name if team else "No team")

def update_team():
    with Session(engine) as session:
        statement = select(Team).where(Team.id == 1)
        team = session.exec(statement).first()
        # print(team.name)
        team.country = "Canada"
        session.add(team)
        session.commit()

def update_data_connection():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.id == 3)
        result = session.exec(statement).first()
        result.team_id = 1
        session.add(result) 
        session.commit()

def remove_data_connection():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.id == 3)
        result = session.exec(statement).first()
        result.team_id = None
        session.add(result)
        session.commit()

def delete_tables():
    with Session(engine) as session:
        model_to_delete = SQLModel.metadata.tables['team']
        SQLModel.metadata.drop_all(bind=engine, tables=[model_to_delete])
        session.commit()

def main():
    # create_db_and_tables()
    # create_teams_and_heros()
    # get_hero_by_where()
    # get_hero_by_join()
    # get_hero_by_left_join()
    # update_team()
    # update_data_connection()
    # remove_data_connection()
    delete_tables()
    

if __name__ == "__main__":
    main()
    # print(__name__)