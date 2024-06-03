"""test_file_storage"""
import unittest
import os
from models.engine.file_storage import FileStorage



class TestFileStorage(unittest.TestCase):
    def test_init(self):
        """was a new FileStorage created"""
        file = FileStorage()
        self.assertIsInstance(file, FileStorage)

    def test_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_file_path_exists(self):
        """Tests an instance of FileStorage to see if the private
        "file_path" attribute is "file.json"."""
        self.assertTrue(os.path.exists("file.json"))

if __name__ == "__main__":
    unittest.main()
