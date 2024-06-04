#!/usr/bin/python3
import uuid
from datetime import datetime
import models
""" BaseModel class, where other
classes will inherit"""


class BaseModel():
    """Base Model Class"""

    def __init__(self, *args, **kwargs):
        """Base Model Class Initialization
        Unique identifier is assigned to the instance
        sets created_at and updated_at attribute to the current date and time
        assigns datetime to created_at updated_at in a string
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = self.updated_at = datetime.now()
        else:
            models.storage.new(self)

    def to_dict(self):
        """converts an instance of a class into a dict representation"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """provides human readable prepresentation of an obj"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)

    def save(self):
        """Update updated_at with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()
