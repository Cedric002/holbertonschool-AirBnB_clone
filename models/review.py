#!/usr/bin/python3
"""
New Class Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    New class Review that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""