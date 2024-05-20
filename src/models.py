import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(20), primary_key=True)
    email = Column(String(20), primary_key=True)
    password = Column(String(20), nullable=False)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    datejoined = Column(String(20), nullable=False)
    favorites = relationship('Favorite') # un usuario puede tener uno o muchos favoritos

class Species(Base): #especies
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(String(200), nullable=True)
    characters = relationship('Character') #una especie puede tener multiples personajes

class Character(Base): #personajes
    __tablename__='character'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(String(30), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    species_id = Column(Integer, ForeignKey('species.id'))
    planet = relationship('Planet')
    favorites = relationship('Favorite')


class Planet(Base): #planetas
    __tablename__='planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    descritpion = Column(String(20), nullable=False)
    clima = Column(String(20), nullable=False)
    terrain = Column(String(20), nullable=False)
    characters = relationship('Character') #un planeta puede tener multiples personajes
    favorites = relationship('Favorite')


class Favorite(Base):
    __tablename__='favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet'))
    user = relationship('User')
    character = relationship('Character')
    planet = relationship('Planet')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
