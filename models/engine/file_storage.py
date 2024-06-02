#!/usr/bin/python3
"""This module defines the class FileStorage"""
import json
# from models import storage


class FileStorage():
    """File Storage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        objects_dict = {}
        for key in self.__objects:
            obj = self.__objects[key]
            objects_dict[key] = obj.to_dict()
        try:
            with open(self.__file_path, 'w') as file:
                json.dump(objects_dict, file)
            print("Success!")
        except Exception as e:
            print("failed")

    def reload(self):
        pass
