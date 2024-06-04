"""module for test_base"""
import unittest
from models.base_model import BaseModel


class Test_Base(unittest.TestCase):
    """Base Model Class"""


    def test_init(self):
        """was a new base created"""
        base = BaseModel()
        self.assertTrue(isinstance(base, BaseModel))

    def test_save(self):
        """test save method of BaseModel"""
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_to_dict(self):
        a = BaseModel()
        a_dict = a.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertIsInstance(a_dict["updated_at"], str)
        self.assertIsInstance(a_dict["created_at"], str)
