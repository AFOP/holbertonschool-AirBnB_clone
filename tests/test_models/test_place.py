#!/usr/bin/python3
""" Test for models/base_model.py"""
import unittest
import os
from models.place import Place


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
        my_state = Place()
        self.assertIsInstance(my_state, Place)

    def test_set(self):
        """check if the class has attribute"""
        my_set = Place()
        my_set.city_id = "Pasto-123-N"
        my_set.user_id = "Pasto-123-N"
        my_set.name = "Andrés"
        my_set.description = "Pasto its in Colombia"
        my_set.number_rooms = 2
        my_set.number_bathrooms = 1
        my_set.max_guest = 1
        my_set.price_by_night = 200
        my_set.latitude = 2.3
        my_set.longitude = 3.2
        my_set.amenity_ids = [12, 13, 14]
        my_dict = my_set.to_dict()
        self.assertIn('city_id', my_dict)
        self.assertIn('user_id', my_dict)
        self.assertIn('name', my_dict)
        self.assertIn('description', my_dict)
        self.assertIn('number_rooms', my_dict)
        self.assertIn('number_bathrooms', my_dict)
        self.assertIn('max_guest', my_dict)
        self.assertIn('price_by_night', my_dict)
        self.assertIn('latitude', my_dict)
        self.assertIn('longitude', my_dict)
        self.assertIn('amenity_ids', my_dict)
        number_int = 0
        my_type = type(my_set.number_rooms)
        self.assertEqual(my_type, type(number_int))
        my_type = type(my_set.number_bathrooms)
        self.assertEqual(my_type, type(number_int))
        my_type = type(my_set.max_guest)
        self.assertEqual(my_type, type(number_int))
        my_type = type(my_set.price_by_night)
        self.assertEqual(my_type, type(number_int))
        number_float = 0.0
        my_type = type(my_set.latitude)
        self.assertEqual(my_type, type(number_float))
        my_type = type(my_set.longitude)
        self.assertEqual(my_type, type(number_float))
        my_list = []
        my_type = type(my_set.amenity_ids)
        self.assertEqual(my_type, type(my_list))


if __name__ == '__main__':
    unittest.main()
