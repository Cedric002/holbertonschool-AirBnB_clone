#!/usr/bin/python3
"""
Base model for the Airbnb console
"""
import json

class BaseModel:
	"""
	The base class of the project
	"""

	def __init__(self, id, created_at, updated_at):
		self.id = id
		self.created_at = created_at
		self.updated_at = updated_at
	
	def save(self):
		pass

	def to_dict(self):
		pass