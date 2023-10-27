#!/usr/bin/python3
"""Testing base model App. """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
 

class test_basemodel(unittest.TestCase):
    """Test base model"""

    def __init__(self, *args, **kwargs):
        """The __init__ method."""
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        """Testing setup."""
        pass

    def tearDown(self):
        """Testing tear down."""
        try:
            os.remove("file.json")
        except:
            pass

    def test_default(self):
        """Testing default."""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Testing kwargs."""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Testing kwargs int."""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Testing save"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open("file.json", "r") as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Testing that returns string."""
        i = self.value()
        self.assertEqual(str(i), "[{}] ({}) {}".format(self.name, i.id, i.__dict__))

    def test_todict(self):
        """Testing to dict."""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Testing kwargs None."""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Testing kwargs one."""
        n = {"Name": "test"}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Testing ID."""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Testing created at."""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Testing updated at."""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
