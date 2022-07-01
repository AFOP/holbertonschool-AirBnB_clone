#!/usr/bin/python3
# defines all common attributes/methods for other classes


import uuid
from datetime import datetime

class BaseModel():
    # class BaseModel

    def __init__(self, *args, **kwargs):
    # method constructor with arguments

        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self):
    # method magic for print class id and dictionary

        return "[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
    # method updates the updated_at with the current datetime

        self.updated_at = datetime.now()

    def to_dict(self):
    # returns a dictionary containing all keys/values of __dict__ of the instance

        if self.__dict__ is None:
            return None
        d = self.__dict__
        for key in d:
            if key == 'created_at' or key == 'updated_at':
                d[key] = datetime.now().isoformat()
        d['__class__'] = BaseModel.__name__
        return d
