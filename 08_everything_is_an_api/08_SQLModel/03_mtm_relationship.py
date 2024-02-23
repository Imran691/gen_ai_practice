from sqlmodel import create_engine, SQLModel, Field, Relationship, Session, select
from typing import Optional
from conn_str import conn_str


class PlayerTeamLink(SQLModel, table=True):
    team_id : Optional[int] = Field(default=None, primary_key=True, foreign_key="team.id")
    hero_id : Optional[int] = Field(default=None, primary_key=True, foreign_key="player.id")

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    country: str
    players: list["Player"] = Relationship(back_populates="teams", link_model=PlayerTeamLink)

class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: Optional[int] = None
    teams : Optional[list[Team]] = Relationship(back_populates="players", link_model=PlayerTeamLink)

engine = create_engine(conn_str, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_teams_and_players():
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", country="USA")
        team_z_force = Team(name="Z-Force", country="CAD")

        player_deadpond = Player(
            name="Deadpond",
            age=35,
            teams=[team_z_force, team_preventers],
        )
        player_rusty_man = Player(
            name="Rusty-Man",
            age=48,
            teams=[team_preventers],
        )
        player_spider_boy = Player(
            name="Spider-Boy", teams=[team_preventers]
        )

        session.add_all([team_preventers, team_z_force, player_deadpond, player_rusty_man, player_spider_boy])
        session.commit()

def update_player():
    with Session(engine) as session:
        player_spider_boy = session.exec(
            select(Player).where(Player.name == "Spider-Boy")
        ).one()
        team_z_force = session.exec(select(Team).where(Team.name == "Z-Force")).one()

        team_z_force.players.append(player_spider_boy)
        session.add(team_z_force)
        session.commit()

        print("Updated Spider-Boy's Teams:", player_spider_boy.teams)
        print("Z-Force heroes:", team_z_force.players)

def delete_tables():
    with Session(engine) as session:
        model_to_delete = SQLModel.metadata.tables['playerteamlink']
        SQLModel.metadata.drop_all(bind=engine, tables=[model_to_delete])
        session.commit()
        model_to_delete = SQLModel.metadata.tables['team']
        SQLModel.metadata.drop_all(bind=engine, tables=[model_to_delete])
        session.commit()
        model_to_delete = SQLModel.metadata.tables['player']
        SQLModel.metadata.drop_all(bind=engine, tables=[model_to_delete])
        session.commit()
        
def main():
    # create_db_and_tables()
    # create_teams_and_players()
    # update_player()
    delete_tables()

if __name__ == "__main__":
    main()