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

    def test_file_path(self):
        """method test__file_path if exist"""

        name_exist = BaseModel()
        name_exist.save()
        self.assertTrue(os.path.exists('file.json'))
        obj_exist = FileStorage()
        obj_exist.reload() 
        print(FileStorage.__objects)


if __name__ == '__main__':
    unittest.main()
