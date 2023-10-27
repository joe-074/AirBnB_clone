#!/usr/bin/python3
"""Testing state App. """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test state that inherits from another class called test_basemodel."""

    def __init__(self, *args, **kwargs):
        """The __init__ method."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Testing name 3."""
        new = self.value()
        self.assertEqual(type(new.name), str)
