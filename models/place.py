#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="all, delete")
    place_amenity = Table("place_amenity", Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"), primary_key=True,  nullable=False),
        Column("amenity_id",String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False )
        )
    amenities = relationship("Amenity", secondary="place_amenity", backref= "places", viewonly=False)
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def reviews(self):
        """getter attribute reviews that returns the list of Review instances with place_id equals to the current Place.id => It will be the FileStorage relationship between Place and Review"""
        from models.engine.file_storage import FileStorage
        reviews_list = []
        data = FileStorage.all(Place)
        for i in data:
            if self.id == i['place_id']:
                reviews_list += [i['review']]
        return reviews_list

#still workin here
    @property
    def amenities(self):
        """handles append method for adding an Amenity.id to the attribute amenity_ids. This method should accept only Amenity object, otherwise, do nothing."""
        from models.amenity import Amenity
        amen_list = []
        data = FileStorage.all(Amenity)
        return amen_list
    @amenities.setter
    def amenities():
        


# Getter attribute amenities that returns the list of Amenity instances based on the attribute amenity_ids that contains all Amenity.id linked to the Place
# Setter attribute amenities that handles append method for adding an Amenity.id to the attribute amenity_ids. This method should accept only Amenity object, otherwise, do nothing.
