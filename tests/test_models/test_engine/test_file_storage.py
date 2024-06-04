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

    def test_save(self):
        """ test file_storage save method """
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", mode="r", encoding="utf-8") as file:
            file_content = file.read()
        self.assertTrue(len(file_content) > 0)
        self.assertIn(f"{self.model.__class__.__name__}.{self.model.id}",
                      file_content)

    def test_reload(self):
        """ test file_storage reload method """
        self.storage.destroy_all()
        self.assertEqual(self.storage.all(), {})
        self.assertTrue(len(self.storage.all()) == 0)
        self.storage.reload()
        self.assertIn(f"{self.model.__class__.__name__}.{self.model.id}",
                      self.storage.all().keys())

if __name__ == '__main__':
    unittest.main()
