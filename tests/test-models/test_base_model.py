"""module for test_base"""

import unittest
import uuid
import datetime
from models.base_model import BaseModel

base = BaseModel()


class BaseModel():
    """Base Model Class"""


    def test_id(self):
        """was a new base created"""
        modell = BaseModel()
        self.assertIsNotNone(modell.id)

    def test_save(self):
        """test save method of BaseModel"""
        base.save()
        self.assertNotEqual(self.model.created_at, self.model.updated_at)
