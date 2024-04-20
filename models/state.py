#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    # Use backref to automatically create a 'state' attribute in the City class
    cities = relationship("City", backref='state', cascade="all, delete")

    name = ""

    def cities(self):
        """getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id
        => It will be the FileStorage relationship between State and City"""
        from models.engine.file_storage import FileStorage
        cities_list = []
        data = FileStorage.all(City)
        for i in data:
            if self.id == i['state_id']:
                cities_list += [i['name']]
        return cities_list
