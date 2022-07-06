#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """method constructor with arguments"""
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key != '__class__':
                    kwargs[key] = value
                format = '%Y-%m-%dT%H:%M:%S.%f'
                if key == 'created_at':
                    value = datetime.strptime(value, format)
                if key == 'updated_at':
                    value = datetime.strptime(value, format)
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
        d = self.__dict__
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
