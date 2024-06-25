#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
import os

if os.getenv('HBNB_TYPE_STORAGE') == "db":
    class Amenity(BaseModel, Base):
        """amenty class"""
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
else:
    class Amenity(BaseModel):
        name = ""
