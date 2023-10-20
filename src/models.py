import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
    __tablename__="user"
    id=Column(Integer(), primary_key=True)
    user_name=Column(String(90), nullable=False, unique=True)
    email=Column(String(90), nullable=False, unique=True)
    password=Column(String(90), nullable=False, unique=True)
    favorite= relationship("Favorites", uselist=True, backref="user")


class Planets(Base):
    __tablename__="planets"
    id=Column(Integer(), primary_key=True)
    planet_name=(Column(String(90), nullable=False, unique=True))
    population=(Column(Integer(), nullable=False))
    climate=Column(String(20), nullable=False)
    favorite=relationship("Favorites", uselist=True, backref="planets")


class Characters(Base):
    __tablename__="characters"
    id=Column(Integer(), primary_key=True)
    name=Column(String(90), nullable=False, unique=True)
    eye_color=Column(String(20), nullable=False)
    gender=Column(String(20), nullable=False)
    favorite=relationship("Favorites", uselist=True, backref="characters")

class Favorites(Base):
    __tablename__="favorites"
    id=Column(Integer(), primary_key=True)
    user_id=Column(Integer(), ForeignKey("user.id"))
    planet_id=Column(Integer(), ForeignKey("planets.id"))
    character_id=Column(Integer(), ForeignKey("characters.id"))







## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
