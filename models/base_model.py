#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime
from xmlrpc.client import _datetime_type
from models import storage


class BaseModel:
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """method constructor with arguments"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    format = "%Y-%m-%dT%H:%M:%S.%f"
                    datetime_obj = datetime.strptime(value, format)
                    setattr(self, key, datetime_obj)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """method magic for print class id and dictionary"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__)

    def save(self):
        """
        method updates the updated_at with the current datetime
        save the objet
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        d = dict(self.__dict__)
        d['__class__'] = self.__class__.__name__
        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
        return d
