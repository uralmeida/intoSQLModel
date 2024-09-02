from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine

class Hero(SQLModel, table =True):
    id:Optional[int] = Field(default=None, primary_key=True )
    name: str
    secret_name: str
    age: Optional[int] = None

engine = create_engine("sqlite:///database.db", echo=True)

SQLModel.metadata.create_all(engine)

hero_1 = Hero(name="Denis", secret_name="Daniel Nunes")
hero_2 = Hero(name="Wonverine", secret_name="James Howlett")
hero_3 = Hero(name="Mestre Kame", secret_name="Muten Roshi", age= 300)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()