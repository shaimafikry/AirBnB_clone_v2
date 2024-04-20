#!/usr/bin/python3
""" creating a database using sql with python"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session , sessionmaker , scoped_session
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel , Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


# script that prints the State object with the name
# passed as argument from the database hbtn_0e_6_usa
class DBStorage ():
    """ the new engine"""
    __engine=None
    __session=None
    def __init__(self):
        """constructor of engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        paswd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://"+user+':'+paswd+'@'+host+'/'+database, pool_pre_ping=True,)
        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine)
        self.__session = scoped_session(session)

            
    def all(self, cls=None):
        """get all data on the current session"""
        dict_ins = {}
        name = cls.__name__
        
        if cls:
            data = self.__session.query(cls).all()
            for i in data:
                key = name + '.'+ i.id
                dict[key] = i
            return dict_ins
        else:
            dict_ins = {}
            classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
            for value in classes.values():
                data = self.__session.query(value).all()
                name = cls.__name__
                key = name + '.'+ value.id
                for i in data:
                    key = name + '.'+ i.id
                    dict[key] = i
            return dict_ins


    def new(self, obj):
        """ add the object to the current database session (self.__session) """
        # cls_name = obj.__class__.__name__
        self.__session.add(obj)


    def save(self):
        """commit all changes of the current database session (self.__session)"""
        self.__session.commit()


    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
            self.__session.commit()


    def reload(self):
        """import the data back"""
        Base.metadata.create_all(self.__engine)
        sessionmaker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessionmaker)
        self.__session = Session(self.__engine)
