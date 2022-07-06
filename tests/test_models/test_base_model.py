#!/usr/bin/python3
""" Test for models/base_model.py"""
import unittest
from models.base_model import BaseModel


class  General(unittest.TestCase):
    "Test Class General"

    def  test_to_dict(self):
        "method test to_dict"

        my_model = BaseModel()
        self.assertTrue(my_model.to_dict())

    def  test_str(self):
        "method test__str"

        my_model = BaseModel()
        my_model.my_number = 89
        my_model.name = "My First Model"
        my_dict = my_model.to_dict()
        self.assertIn('name', my_dict)
        self.assertIn('my_number', my_dict)
        self.assertIn('id', my_dict)
        self.assertIn('created_at', my_dict)
        self.assertIn('updated_at', my_dict)

if __name__ == '__main__':
        unittest.main()