"""module for test_base"""

import unittest
import uuid
import datetime
from models.base_model import BaseModel

base = BaseModel()


class Test_Base(unittest.TestCase):
    """Base Model Class"""


    def test_init(self):
        """was a new base created"""
        self.assertTrue(isinstance(base, BaseModel))

    def test_save(self):
        """test save method of BaseModel"""
        a = BaseModel()
        initial = a.updated_at
        a.save()
        stored = a.updated_at
        self.assertNotEqual(initial,stored)
