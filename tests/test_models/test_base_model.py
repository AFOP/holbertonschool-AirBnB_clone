#!/usr/bin/python3
""" Test for models/base_model.py"""
import unittest
import os
from models.base_model import BaseModel


class  General(unittest.TestCase):
    "Test Class General"

    def test_executable_file(self):
        "test_executable_file"

        is_read_true = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(is_read_true)

        is_write_true = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(is_write_true)

        is_exec_true = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_id(self):
        "method test id"
        my_model1 = BaseModel()
        self.assertIsInstance(my_model1, BaseModel)
        my_model2 = BaseModel()
        self.assertNotEqual(my_model1.id, my_model2.id)

    def  test_to_dict(self):
        "method test to_dict"

        my_model = BaseModel()
        my_dict = my_model.to_dict()
        self.assertIsInstance(my_dict, dict)
        for key, value in my_dict.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)
            if key == 'id':
                self.assertIsInstance(value, str)

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

    def test_save(self):
        "method test__save"
        my_model = BaseModel()
        first_updated = my_model.updated_at
        my_model.save()
        second_updated = my_model.updated_at
        self.assertNotEqual(first_updated, second_updated)

if __name__ == '__main__':
        unittest.main()