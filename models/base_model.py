#!/usr/bin/python3
"""
Base model for the Airbnb console
"""
import json

class BaseModel:
	"""
	The base class of the project
	"""

	def __init__(self, *args, **kwargs):
        if kwargs:
            for attr_name, attr_value in kwargs.items():
                if attr_name != "__class__":
                    setattr(self, attr_name, attr_value)

            # Convert created_at and updated_at strings to datetime objects
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            # Create id and created_at attributes
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
	
	def save(self):
		pass

	def to_dict(self):
		pass
