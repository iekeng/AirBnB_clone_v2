#!/usr/bin/python3
import uuid
from datetime import datetime
"""Defines BaseModel Class"""


class BaseModel:
    """Represents the BaseModel of HBnB"""
    id = str(uuid.uuid4())
    created_at = datetime.today()
    updated_at = datetime.today()

    def save(self):
        """Updates 'updated_at' with current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns the dictionary if the BaseModel instance"""
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.updated_at.isoformat()
        dic["updated_at"] = self.created_at.isoformat()
        return dic

    def __str__(self):
        """Return the str representation of the BaseModel instance"""
        cname = self.__class__.__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)
