#!/usr/bin/python3
""" Test for models/base_model.py"""
import unittest
import os
from models.state import State


class General(unittest.TestCase):
    """Test Class General"""

    def test_executable_file(self):
        """test_executable_file"""

        is_read_true = os.access('models/user.py', os.R_OK)
        self.assertTrue(is_read_true)

        is_write_true = os.access('models/user.py', os.W_OK)
        self.assertTrue(is_write_true)

        is_exec_true = os.access('models/user.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """check if my_model is an instance of BaseModel"""
        my_state = State()
        self.assertIsInstance(my_state, State)

    def test_set(self):
        """check if the class has attribute"""
        my_set = State()
        self.assertIsInstance(my_set.name, str)
        my_set.name = "Andrés"
        my_dict = my_set.to_dict()
        self.assertIn('name', my_dict)


if __name__ == '__main__':
    unittest.main()
