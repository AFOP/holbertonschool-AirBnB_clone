#!/usr/bin/python3

"""class State that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """class State that inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
