#!/usr/bin/python3
'''the State model'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
'''class for all tables'''


class State(Base):
    '''row in a states table'''
    __tablename__ = "states"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(length=128),
        nullable=False
    )
    cities = relationship(
        "City",
        cascade="all, delete, delete-orphan",
        backref="state"
    )
