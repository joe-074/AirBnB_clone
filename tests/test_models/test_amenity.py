#!/usr/bin/python3
"""Testing amenity App. """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test Amenity that inherits from another class called test_basemodel."""

    def __init__(self, *args, **kwargs):
        """The __init__ method."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """The test_name2 method creates a new object using the self.value attribute."""
        new = self.value()
        self.assertEqual(type(new.name), str)
