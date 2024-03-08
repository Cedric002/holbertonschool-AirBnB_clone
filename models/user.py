#!/usr/bin/python3
"""
New Class User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    New class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""