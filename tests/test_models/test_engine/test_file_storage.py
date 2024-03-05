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
	
	def test_object(self):
		file_object = FileStorage()
		self.assertIsInstance(file_object._FileStorage__objects, dict)
	
	def test_all(self):
		file_storage = FileStorage()
		all_objects = file_storage.all()
		self.assertIsInstance(all_objects, dict)
		self.assertIs(all_objects, file_storage._FileStorage__objects)

	def test_new(self):
		file_storage = FileStorage()
		base_model = BaseModel()
		file_storage.new(base_model)
		obj_key = "BaseModel." + base_model.id
		self.assertIn(obj_key, file_storage._FileStorage__objects)

	def test_save(self):
		pass

	def test_reload(self):
		pass

if __name__ == "__main__":
    unittest.main()