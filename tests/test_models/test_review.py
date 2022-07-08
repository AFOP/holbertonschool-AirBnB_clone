#!/usr/bin/python3
""" Test for models/base_model.py"""
import unittest
import os
from models.review import Review


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
        my_state = Review()
        self.assertIsInstance(my_state, Review)

    def test_set(self):
        """check if the class has attribute"""
        my_set = Review()
        my_set.place_id = "Pasto-123-N"
        my_set.user_id = "Pasto-123-N"
        my_set.text = "Andrés"
        my_dict = my_set.to_dict()
        self.assertIn('place_id', my_dict)
        self.assertIn('user_id', my_dict)
        self.assertIn('text', my_dict)


if __name__ == '__main__':
    unittest.main()
