#!/usr/bin/python3
"""This module defines the class FileStorage"""
import json
from models.base_model import BaseModel
# from models import storage


class FileStorage():
    """File Storage Class"""
    def __init__(self, file_path, objects):
        self.file_path = file_path
        # string (path to the JSON file (ex: file.json))
        self.objects = objects
        # dictionary (empty byt will store all objects by <class name>.id
        # (ex: to store a BaseModel object with id=12121212, the key will be BaseMode.12121212))

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        self.__file_path = value

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):

        self.__objects = value

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.objects[key] = obj
