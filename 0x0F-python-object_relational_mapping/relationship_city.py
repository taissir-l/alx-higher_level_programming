#!/usr/bin/python3
'''the City model'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from relationship_state import Base


class City(Base):
    '''row in a cities table'''
    __tablename__ = "cities"
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
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
