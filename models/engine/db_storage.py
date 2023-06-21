#!/usr/bin/python3
"""Creating a new engine DBStorage"""
import os
import ast
from models.base_model import Base
from sqlalchemy import create_engine


class DBStorage:
    """Class representing a database storage engine"""

    __engine = None
    __session = None

    def __init(self):
        """initializes a new instance"""
        self.__engine = create_engine("mysql+mysqldb: // {}:
                                      {}@localhost:  3306/{}".
                                      format(os.environ.get('HBNB_MYSQL_USER'),
                                      os.environ.get('HBNB_MYSQL_PWD'),
                                      os.environ.get('HBNB_MYSQL_HOST'),
                                      os.environ.get('HBNB_MYSQL_DB'))
                                      pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') == test:
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries the database"""
        if cls:
            results = self.__session.query(ast.literal_eval(cls)).all()
        else:
            results = self.__session.query(User, State, City,
                                           Amenity, Place, Review).all()
        return (f"{type(obj).__name__}.{obj.id}": obj for obj in results)
