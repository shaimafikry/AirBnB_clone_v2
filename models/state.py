#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import os
import models

if os.getenv('HBNB_TYPE_STORAGE') == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        # Use backref to automatically create a 'state'
        # attribute in the City class
        cities = relationship("City", backref='state')
else:
    class State(BaseModel):
        name = ""

        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id
            => It will be the FileStorage relationship between
            State and City"""
            cities_list = []
            data = models.storage.all(City)
            for i in data.values():
                if self.id == i.state_id:
                    cities_list.append(i)
            return cities_list
