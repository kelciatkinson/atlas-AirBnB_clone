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
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.storage.new(self.obj)
        self.assertIn(key, self.storage.all())
    
    def test_all(self):
        pass

    def test_save(self):
        pass

    def test_reload(self):
        """ test file_storage reload method """
        pass

if __name__ == '__main__':
    unittest.main()
