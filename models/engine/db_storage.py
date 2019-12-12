#!/usr/bin/python3
"""Database storage"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ Database storage
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.
            format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dictionary = {}
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for _class in [State, City, User, Place, Review]:
                for obj in self.__session.query(_class):
                    objects.append(obj)
        for obj in objects:
            key = type(obj).__name__ + '.' + obj.id
            dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """serialize the file path to JSON file path
        """
        self.__session.commit()

    def reload(self):
        """serialize the file path to JSON file path
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
        )
        self.__session = Session()

    def delete(self, obj=None):
        """Deletes obj from __objects"""
        if obj:
            self.__session.delete(obj)
