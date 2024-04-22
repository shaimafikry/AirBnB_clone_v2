#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

# association table
place_amenity = Table("place_amenity", Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"), primary_key=True,  nullable=False),
        Column("amenity_id",String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False )
        )
    
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


    # relationships
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity", backref= "place_amenities", viewonly=False)
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
        """getter that returns the list of Amenity instances based on the attribute amenity_ids that contains all Amenity.id linked to the Place"""
        from models.amenity import Amenity
        list_obj = []
        for i in self.amenity_ids:
            #gets the instances based on their id
            list_obj += [Amenity.objects.get(id=i)]
        return list_obj
    @amenities.setter
    def amenities(self, obj):
        from models.amenity import Amenity
        """Setter attribute amenities that handles append method for adding an Amenity.id to the attribute amenity_ids. This method should accept only Amenity object, otherwise, do nothing."""
        if isinstance(obj, Amenity):
            #appeneds to the list of amenity_ids
            self.amenity_ids.append(obj.id)
