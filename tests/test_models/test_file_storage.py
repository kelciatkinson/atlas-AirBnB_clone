"""test_file_storage"""
import unittest
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    def test_init(self):
        """was a new FileStorage created"""
        file = FileStorage()
        self.assertIsInstance(file, FileStorage)
