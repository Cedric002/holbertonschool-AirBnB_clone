#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import sys
import os
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    The the BaseModel class
    """
    base_model = BaseModel()

        # Check if the ID is generated (not None)
        self.assertIsNotNone(base_model.id)

    def test_to_dict(self):
        # Create an instance of BaseModel
        base_model = BaseModel()

        # Convert to dictionary
        base_dict = base_model.to_dict()

        # Check if 'id' and 'created_at' keys are present
        self.assertIn('id', base_dict)
        self.assertIn('created_at', base_dict)

    def test_save(self):
        """
        Test the save updated_at function
        """
        first_updated_at = BaseModel().updated_at
        BaseModel()
        new_updated_at = BaseModel().updated_at
        self.assertNotEqual(first_updated_at, new_updated_at)


if __name__ == "__main__":
    unittest.main()
