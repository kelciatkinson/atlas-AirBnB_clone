"""test_file_storage"""
import unittest
import os
import json
import models
from models.engine.file_storage import FileStorage
from models import storage
from models.engine import file_storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


class TestFileStorage(unittest.TestCase):
    def test_init(self):
        """was a new FileStorage created"""
        file = FileStorage()
        self.assertIsInstance(file, FileStorage)

    def test_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_all(self):
        """ test all method """
        model = BaseModel()
        my_dict = self.storage.all()
        self.assertIsInstance(my_dict, dict)
        self.assertIn(model, my_dict.values())

    def test_save(self):
        """test save method for file_storage"""
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.storage.new(self.obj)
        self.storage.save()
        self.assertEqual(self.storage.all()[key].id, self.obj.id)

    def test_reload(self):
        """test reload method for file_storage"""
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.storage.new(self.obj)
        self.storage.save()
        storage_2 = FileStorage()
        storage_2.reload()
        reloaded_obj = storage_2.all()[key]
        self.assertEqual(reloaded_obj.id, self.obj.id)
        self.assertEqual(reloaded_obj.to_dict(), self.obj.to_dict())

    def test_new(self):
        """test new method for file_storage"""
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.storage.new(self.obj)
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
