#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """amenty class"""
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""
