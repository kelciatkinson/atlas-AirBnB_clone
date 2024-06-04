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
        all_obj = self.storage.all()
        key = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.storage.new(self.obj)
        all_objects = self.storage.all()
        self.assertEqual(all_objects[key], self.obj)

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
        key = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.storage.new(self.obj)
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
