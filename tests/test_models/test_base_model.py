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
