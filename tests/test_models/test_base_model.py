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
