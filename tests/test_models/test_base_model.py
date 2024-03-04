#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import uuid
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.my_model = BaseModel()

    def test_save(self):
        """
        Test that save() method updates updated_at attribute
        """
        original_updated_at = self.my_model.updated_at
        self.my_model.save()
        new_updated_at = self.my_model.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

    def test_to_dict(self):
        my_model_dict = self.my_model.to_dict()
        expected_output = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_output:
            self.assertIn(key, my_model_dict)
        self.assertIsInstance(my_model_dict['id'], str)
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)
        self.assertIsInstance(my_model_dict['__class__'], str)

     def test_to_dict(self):
        # Create an instance of BaseModel
        base_model = BaseModel()

        # Convert to dictionary
        base_dict = base_model.to_dict()

        # Check if 'id' and 'created_at' keys are present
        self.assertIn('id', base_dict)
        self.assertIn('created_at', base_dict)

    def test__str__(self):
        expected_output = "[BaseModel] ({}) {}".format(self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_output)
