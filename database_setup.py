from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#PLACE YOUR TABLE SETUP INFORMATION HERE

class Person(Base):
    __tablename__ = 'person'
    name = Column(String)
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    gender = Column(String)
    nationality = Column(String)
    city = Column(String)  # city/town name
    phone = Column(String)
    instrument = Column(String)
    DOB = Column(String) #change
    tv_shows = Column(String)


