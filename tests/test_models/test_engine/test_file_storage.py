#!/usr/bin/python3
"""Test for engine/file_storage.py"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class General(unittest.TestCase):
    """Test Class General"""

    def test_executable_file(self):
        """test_executable_file"""

        is_read_true = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(is_read_true)

        is_write_true = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(is_write_true)

        is_exec_true = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_save(self):
        """method test__str"""

        my_model = BaseModel()
        my_model.save()
        self.assertTrue(os.path.exists('file.json'))
    
    def test_class(self):
        """method test__str"""

        my_model = BaseModel()
        name_class = type(my_model)
        self.assertEqual(name_class, BaseModel)
        my_model = Amenity()
        name_class = type(my_model)
        self.assertEqual(name_class, Amenity)
        my_model = City()
        name_class = type(my_model)
        self.assertEqual(name_class, City)
        my_model = Place()
        name_class = type(my_model)
        self.assertEqual(name_class, Place)
        my_model = Review()
        name_class = type(my_model)
        self.assertEqual(name_class, Review)
        my_model = State()
        name_class = type(my_model)
        self.assertEqual(name_class, State)
        my_model = User()
        name_class = type(my_model)
        self.assertEqual(name_class, User)


if __name__ == '__main__':
    unittest.main()
