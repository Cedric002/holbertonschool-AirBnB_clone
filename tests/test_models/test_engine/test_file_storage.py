#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import uuid
from models.base_model import BaseModel
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
	def test_path(self):
		file_storage = FileStorage()
		expected_file_storage = 'file.json'
		self.assertEqual(file_storage._FileStorage__file_path, expected_file_storage)

if __name__ == "__main__":
    unittest.main()