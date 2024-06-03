#!/usr/bin/python3
"""test_city"""
import unittest
import os
import models.engine.file_storage import FileStorage
from models.city import City


class TestCity(unittest.TestCase):
    """Test the class City"""

    def test_init(self):
        """unit tests for city"""
        city = City()
        self.assertTrue(hasattr(city, 'name'))
        self.assertTrue(hasattr(city, 'state_id'))
