#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel():
    """Base Model Class"""
    
    def __init__(self, *args, **kwargs):
        """Base Model Class Initialization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format(__class__ ,self.id, self.__dict__))

    def save(self):
        """Update updated_at with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
