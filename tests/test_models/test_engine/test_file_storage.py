"""test_file_storage"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models import storage
from models.engine import file_storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def test_init(self):
        """was a new FileStorage created"""
        file = FileStorage()
        self.assertIsInstance(file, FileStorage)

    def test_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_all(self):
        """test all method for file_storage"""
        model = Basemodel()
        my_dict = self.storage.all()
        self.assertIsInstance(my_dict, dict)
        self.assertIn(model, myy_dict.values())

    def test_save(self):
        """test save method for file_storage"""
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", mode="r", encoding="utf-8") as file:
            file_content = file.read()
        self.assertTrue(len(file_content) > 0)
        self.assertIn(f"{self.model.__class__.__name__}.{self.model.id}",
            file_content)

    def test_relaod(self):
        """test reload method for file_storage"""
        self.storage.destroy_all()
        self.assertEqual(self.storage.all(), {})
        self.assertTrue(len(self.storage.all()) == 0)
        self.storage.reload()
        self.assertIn(f"{self.model.__class__.__name__}.{self.model.id}",
                self.storage.all().keys())

    def test_new(self):
        """test new method for file_storage"""
        model = BaseModel()
        self.storage.new(model)
        my_dict = self.storage.all()
        self.assertIn(model, my_dict.values())


if __name__ == "__main__":
    unittest.main()
