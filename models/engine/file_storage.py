#!/usr/bin/python3
"""This module defines the class FileStorage"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """File Storage Class to manage serialization
    and deserialization of objects to and from a JSON file"""

    # Private attributes
    __file_path = "file.json"
    __objects = {}

    @property
    def file_path(self):
        return self.__file_path

    def all(self):
        """Returns the dictionary __objects.
        This method provides access to the dictionary "__objects" that
        stores all objects managed by the instance "FileStorage"."""

        return self.__objects

    def new(self, obj):
        """This method adds a new object to the __objects dictionary.
        The object's key isthe class name with object's ID separated
        by a period. The object is the value."""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """This method serializes __objects to the JSON file path
        located in "__file_path" variable."""

        objects_dict = {}
        with open(self.__file_path, 'w') as file:
            for key, value in self.__objects.items():
                objects_dict[key] = value.to_dict()
            json.dump(objects_dict, file)

    def reload(self):
        """This method deserializes the JSON file and populates the
        "__objects" dictionary with objects stored in the JSON file."""

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                objects_dict = json.load(file)
            for key, value in objects_dict.items():
                cls_name = value["__class__"]
                if cls_name == "BaseModel":
                    self.__objects[key] = BaseModel(**value)
                elif cls_name == "User":
                    self.__objects[key] = User(**value)
                elif cls_name == "State":
                    self.__objects[key] = State(**value)
                elif cls_name == "City":
                    self.__objects[key] = City(**value)
                elif cls_name == "Amenity":
                    self.__objects[key] = Amenity(**value)
                elif cls_name == "Place":
                    self.__objects[key] = Place(**value)
                elif cls_name == "Review":
                    self.__objects[key] = Review(**value)
