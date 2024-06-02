"""test_file_storage"""
import unittest
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    def test_init(self):
        """was a new FileStorage created"""
        file = FileStorage()
        self.assertIsInstance(file, FileStorage)

    def test_file_path(self):
        """Tests an instance of FileStorage to see if the private
        "file_path" attribute is "file.json"."""
        file = FileStorage()
        file_path = file._FileStorage__file_path
        self.assertEqual(file_path, "file.json")
