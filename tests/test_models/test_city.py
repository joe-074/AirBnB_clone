#!/usr/bin/python3
"""Testing city App. """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Testing city."""

    def __init__(self, *args, **kwargs):
        """The __init__ method is the constructor of the test_City class."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Testing state id."""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Testing name."""
        new = self.value()
        self.assertEqual(type(new.name), str)
