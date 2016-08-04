from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, Table

Base = declarative_base()

#PLACE YOUR TABLE SETUP INFORMATION HERE


class Person(Base):
	__tablename__ = 'person'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String)
	password = Column(String)
	gender = Column(String)
	nationality = Column(String)
	city = Column(String)  # city/town name
	phone = Column(String)
	instrument = relationship("Instrument", uselist=True, secondary='person_to_instrument', lazy=True)
	genre = Column(String)
	dob = Column(Date) #change
	interests = relationship("Interests", uselist=True, secondary='person_to_interests', lazy=True)

class Interests(Base):
	__tablename__ = 'interests'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	persons = relationship("Person", uselist=True, secondary='person_to_interests', lazy=True)	


class PersonToInterests(Base):
	__tablename__ = 'person_to_interests'
	id = Column(Integer, primary_key=True)
	person_id = Column(Integer, ForeignKey('person.id'))
	interests_id = Column(Integer, ForeignKey('interests.id'))
	person = relationship(Person, uselist=True)
	interest = relationship(Interests, uselist=True)

###

class Instrument(Base):
	__tablename__ = 'instrument'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	persons = relationship("Person", uselist=True, secondary='person_to_instrument')	


class PersonToInstrument(Base):
	__tablename__ = 'person_to_instrument'
	id = Column(Integer, primary_key=True)
	person_id = Column(Integer, ForeignKey('person.id'))
	instrument_id = Column(Integer, ForeignKey('instrument.id'))
	person = relationship(Person, uselist=True)
	instrument = relationship(Instrument, uselist=True)

