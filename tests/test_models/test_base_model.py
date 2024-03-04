#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import uuid
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test the BaseModel class
    """
    def test_save(self):
        """
        Test the save() updated_at function
        """
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        new_updated_at = my_model.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict() function
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["id"], my_model.id)
        self.assertEqual(my_model_json["created_at"], my_model.created_at.isoformat())

    def test__str__(self):
        """Test __str__()"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(str(my_model), "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__))

    def test_init(self):
        """
        Test that the instance has the correct attributes
        """
        self.my_model = BaseModel()
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))


if __name__ == "__main__":
    unittest.main()
