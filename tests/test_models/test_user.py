#!/usr/bin/python3
""" Test for models/base_model.py"""
import unittest
import os
from models.user import User


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
        my_user = User()
        self.assertIsInstance(my_user, User)

    def test_set(self):
        """check if the class has attribute"""
        my_set = User()
        self.assertIsInstance(my_set.email, str)
        self.assertIsInstance(my_set.password, str)
        self.assertIsInstance(my_set.first_name, str)
        self.assertIsInstance(my_set.last_name, str)
        my_set.email = "880204.afop@gmail.com"
        my_set.password = "andres1234"
        my_set.first_name = "Andres"
        my_set.last_name = "Ocaña"
        my_dict = my_set.to_dict()
        self.assertIn('email', my_dict)
        self.assertIn('password', my_dict)
        self.assertIn('first_name', my_dict)
        self.assertIn('last_name', my_dict)


if __name__ == '__main__':
    unittest.main()
