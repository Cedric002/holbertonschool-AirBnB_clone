#!/usr/bin/python3
"""
Base model for the Airbnb console
"""
import json
import uuid
from datetime import datetime

class BaseModel:
	"""
	The base class of the project
	"""

	def __init__(self):
		"""
		Constructor for BaseModel
		"""
		self.id = str(uuid.uuid4)
		self.created_at = datetime.now()
		self.updated_at = datetime.now()
	
	def save(self):
		pass


	def to_dict(self):
		pass

	def __str__(self):
		return "[BaseModel] ({}) {}".format(self.id, self.__dict__)