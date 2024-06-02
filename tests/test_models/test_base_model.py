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
        a = BaseModel()
        initial = a.updated_at
        a.save()
        stored = a.updated_at
        self.assertNotEqual(initial,stored)

    def test_to_dict(self):
        a = BaseModel()
        dictionary = a.to_dict()
        self.assertEqual(dictionary["__class__"], "BaseModel")
        self.assertEqual(dictionary["created_at"], a.created_at.isoformat())
        self.assertEqual(dictionary["updated_at"], a.created_at.isoformat())
