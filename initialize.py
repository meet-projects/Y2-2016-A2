from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Person

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# You can add some starter data for your database here.

jeries = Person(name="jeries", email="jeries_k@gmail.com", password="fghjk5678", gender="male", nationality="palastinian", city="nazareth", phone="45678876545", instrument="violin", DOB="00/00/0000", tv_shows="GOT")

