#!/usr/bin/python3
"""This module defines the class FileStorage"""
from models.base_model import BaseModel
from models.user import User
import json
import os

class FileStorage():
    """File Storage Class"""
    __file_path = "file.json"
    __objects = {}

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        self.__file_path = value

    def all(self):
        """Returns the dictionary __objects. This method provides access to the
        dictionary "__objects" that stores all objects managed by the instance 
        "FileStorage". """
        return self.__objects

    def new(self, obj):
        """This method adds a new object to the __objects dictionary. The key
        for the object is the class name with object's ID separated by a period.
        The value is the object itself."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """This method serializes __objects to the JSON file path:
        "__file_path"."""
        objects_dict = {}
        with open(self.__file_path, 'w') as file:
            for key, value in self.__objects.items():
                objects_dict[key] = value.to_dict()
            json.dump(objects_dict, file)

    def reload(self):
        """This method deserializes the JSON file specified by "__file_path"
        and populates the "__objects" dictionary with objects stored
        in the JSON file."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                objects_dict = json.load(file)
            for key, value in objects_dict.items():
                self.__objects[key] = BaseModel(**value)
