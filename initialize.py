from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

from database_setup import Base, Person, Interests, PersonToInterests, Instrument, PersonToInstrument

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



# You can add some starter data for your database here.

jeries = Person(name="jeries",
				email="jeries_k@gmail.com", 
				password="abc", 
				gender="male", 
				nationality="palastinian", 
				city="nazareth", 
				genre="clasical", 
				phone="45678876545", 
				dob=datetime(2000,5,27))


session.add(jeries)

violin = Instrument(name = "violin")
GOT = Interests(name = "GOT")
jeries.instrument.append(violin)
jeries.interests.append(GOT)

yaniv = Person(name="yaniv",
				email="yanivkapx1@gmail.com", 
				password="yaniv", 
				gender="male", 
				nationality="Israeli", 
				city="Bet Shemesh", 
				genre="Rock", 
				phone="0507183378", 
				dob=datetime(2000,6,24))


session.add(yaniv)

guitar = Instrument(name = "guitar")
HIMYM = Interests(name = "How I met your mother")
yaniv.instrument.append(guitar)
yaniv.instrument.append(violin)
yaniv.interests.append(HIMYM)

session.commit()

# list_of_instruments = session.query(Instrument).filter_by(name = instrument).all()
# list_of_people = []
# for instrument in list_of_instruments:
# 	list_of_people.append(instrument.persons)

# got = Interests(name = "GOT")
# violin = Instrument(name = "violin")

# session.add(violin)

# jeries.interests.append(movie)
# jeries2.interests += [movie, got]


# session.query(Person).delete()
# session.add(movie)
# session.add(got)
# session.add(jeries)
# session.add(jeries2)
# session.commit()


# res = session.query(PersonToInterests).filter_by(interests_id = movie.id).all()
# for r in res:
# 	for p in r.person:
# 		print (p.email)
# res2 = session.query(Interests).all()
# print(res)


# for x in jeries.interests:
# 	print(x.name)


# for x in movie.persons:
# 	print(x.email)