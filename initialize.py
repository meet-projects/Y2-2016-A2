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

jeries = Person(name="Jeries Saleh",
				email="jeries@gmail.com", 
				password="jeries", 
				gender="Male", 
				nationality="Palastinian", 
				city="Jerusalem", 
				genre="clasical", 
				phone="0502846374", 
				dob=datetime(2000,5,27))


session.add(jeries)

oud = Instrument(name = "oud")
violin = Instrument(name = "violin")
friends = Interests(name = "friends")
jeries.instrument.append(violin)
jeries.instrument.append(oud)
jeries.interests.append(friends)

yaniv = Person(name="Yaniv Kapilianov",
				email="yaniv@gmail.com", 
				password="yaniv", 
				gender="Male", 
				nationality="Israeli", 
				city="Jerusalem", 
				genre="Rock", 
				phone="0507183378", 
				dob=datetime(2000,6,24))


session.add(yaniv)

guitar = Instrument(name = "guitar")
voice = Instrument(name = "voice")
HIMYM = Interests(name = "How I met your mother")
yaniv.instrument.append(guitar)
yaniv.instrument.append(voice)
yaniv.interests.append(HIMYM)

tal = Person(name="Tal Bar",
				email="tal@gmail.com", 
				password="Jerusalem", 
				gender="Female", 
				nationality="Israeli", 
				city="Jerusalem", 
				genre="Rock", 
				phone="0507567873", 
				dob=datetime(2000,4,3))


session.add(tal)

drums = Instrument(name = "drums")
flash = Interests(name = "The Flash")
tal.instrument.append(drums)
tal.instrument.append(voice)
tal.interests.append(flash)

yair = Person(name="Yair Shalev",
				email="yair@gmail.com", 
				password="Jerusalem", 
				gender="Male", 
				nationality="Israeli", 
				city="Jerusalem", 
				genre="Rock", 
				phone="05078484489", 
				dob=datetime(1999,7,7))


session.add(yair)

piano = Instrument(name = "piano")
contrabass = Instrument(name = "contrabass")
GOT = Interests(name = "Game Of Thrones")
yair.instrument.append(piano)
yair.instrument.append(contrabass)
yair.interests.append(GOT)

nada = Person(name="Nada Swedan",
				email="nada@gmail.com", 
				password="Jerusalem", 
				gender="Feale", 
				nationality="Palastinian", 
				city="Jerusalem", 
				genre="Rock", 
				phone="05078484489", 
				dob=datetime(1999,7,25))


session.add(nada)

nada.instrument.append(voice)
nada.interests.append(friends)

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