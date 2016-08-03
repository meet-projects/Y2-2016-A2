from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

from database_setup import Base, Person, Interests, PersonToInterests, Instrument, PersonToInstrument

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



# You can add some starter data for your database here.

jeries = Person(name="jeries",
				email="jeries_k@gmail.com", 
				password="fghjk5678", 
				gender="male", 
				nationality="palastinian", 
				city="nazareth", 
				genre="clasical", 
				phone="45678876545", 
				dob=datetime(2000,5,27), 
				tv_shows="GOT")




# movie = Interests(name = "movie")
# got = Interests(name = "GOT")
# violin = Instrument(name = "violin")

# session.add(violin)
# session.add(jeries)

# jeries.instrument.append(violin)
# session.commit()

# inst = session.query(PersonToInstrument).filter_by(instrument_id = violin.id).all()

# for x in inst:
# 	for p in x.person:
# 		print (p.name)



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