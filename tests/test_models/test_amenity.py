"""test_amenity"""
import unittest
import models.amenity
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test the class Amenity"""

    def test_init(self):
        """Test the initialization of Amenity class"""
        self.assertEqual(self.place1.city_id, "")
