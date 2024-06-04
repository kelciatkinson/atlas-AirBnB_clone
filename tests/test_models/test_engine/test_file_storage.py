"""test_file_storage module"""
import unittest
import os
import json
from models import storage
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """TestFileStorage class documentation"""
    def setUp(self):
        """ setup for all tests """
        self.model = BaseModel()
        self.storage = FileStorage()
        self.storage.save()

    def tearDown(self):
        """ teardown for all tests """
        del self.model
        del self.storage
        os.remove("file.json")

    def test_new(self):
        """test new method for file_storage"""
        file = FileStorage()
        self.assertEqual(type(file.file_path), str)
    
    def test_all(self):
        """test all method for file_storage"""
        model = BaseModel()
        my_dict = self.storage.all()
        self.assertIsInstance(my_dict, dict)
        self.assertIn(model, my_dict.values())

    def test_save_and_reload(self):
        """ test file_storage save and reload method """
        key = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.storage.new(self.obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        reloaded_object = new_storage.all()[key]
        self.assertEqual(reloaded_object.id, self.obj.id)
        self.assertEqual(reloaded_object.to_dict(), self.obj.to_dict())

if __name__ == '__main__':
    unittest.main()
