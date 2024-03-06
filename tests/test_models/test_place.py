#!/usr/bin/python3
"""
Module for Place unittest
"""
import uuid
import json
from models.base_model import BaseModel
from models.place import Place
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test the State_id class attr
    """
    def test_user_place(self):
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_user_place_1(self):
        place = Place()
        place.city_id = "France"
        self.assertEqual(place.city_id, "France")
