from sqlmodel import SQLModel, create_engine, Field, Relationship, Session, select
from typing import Optional
from conn_str import conn_str
from typing import List

engine = create_engine(conn_str, echo=True)


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    country: str
    # relationship attribute to define relationships b/w two models
    # in back_populates="team"; "team" is the name of the attribute in the Team model
    hero: List["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    # Optional type annotation means that attribute could be None or a full team object
    # This is becase the team id could be None in DB
    team: Optional[Team] = Relationship(back_populates="hero")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_teams_and_heros():
    with Session(engine) as session:
        # use of relationship skpis adding and committing teams before the heroes
        # We commit once and teams id's are automatically assigned to heroes
        team_1 = Team(name="Avengers", country="USA")
        team_2 = Team(name="X-Men", country="CAD")

        hero_1 = Hero(name="Spider-Man",
                      secret_name="Peter Parker", team=team_1)
        hero_2 = Hero(name="Iron Man", secret_name="Tony Stark", team=team_2)

        session.add_all([team_1, team_2, hero_1, hero_2])
        session.commit()


def update_hero_team():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.id == 1)
        hero = session.exec(statement).first()

        statement_1 = select(Team).where(Team.id == 2)
        team = session.exec(statement_1).first()

        hero.team = team
        session.add(hero)
        session.commit()

# create a team alongwith its list of heros


def create_team_with_heros():
    with Session(engine) as session:
        hero_black_lion = Hero(
            name="Black Lion", secret_name="Tony Stark", age=40)
        hero_pink_panther = Hero(
            name="Pink Panther", secret_name="Tony Stark", age=40)

        team = Team(
            name="Fighters", country="AUS", hero=[hero_black_lion, hero_pink_panther])
        session.add(team)
        session.commit()


def get_team_with_heros():
    with Session(engine) as session:
        statement = select(Team).where(Team.id == 3)
        team = session.exec(statement).first()
        # print(team)
        print(team.hero)

def delete_tables():
    with Session(engine) as session:
        model_to_delete = SQLModel.metadata.tables['team']
        SQLModel.metadata.drop_all(bind=engine, tables=[model_to_delete])
        session.commit()


def main():
    # create_db_and_tables()
    # create_teams_and_heros()
    # update_hero_team()
    # create_team_with_heros()
    # get_team_with_heros()
    delete_tables()


if __name__ == "__main__":
    main()
