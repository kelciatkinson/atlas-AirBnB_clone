"""module for test_base"""
import unittest
import os
from models.base_model import BaseModel


class Test_Base(unittest.TestCase):
    """Base Model Class"""


    def test_init(self):
        """was a new base created"""
        base = BaseModel()
        self.assertTrue(isinstance(base, BaseModel))

    def test_save(self):
        """test save method of BaseModel"""
        my_model = my_model.save()
        one_save = my_model.updated_at
        self.assertTrue(os.path.exists("file.json"))
        two_save = my_model.updated_at
        self.assertNotEqual(one_save, two_save)

    def test_to_dict(self):
        a = BaseModel()
        a_dict = a.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertIsInstance(a_dict["updated_at"], str)
        self.assertIsInstance(a_dict["created_at"], str)
