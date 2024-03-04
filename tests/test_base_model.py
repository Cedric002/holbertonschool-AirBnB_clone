#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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