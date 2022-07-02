#!/usr/bin/python3
# defines all common attributes/methods for other classes


import uuid
from datetime import datetime
import models

class BaseModel():
    # class BaseModel

    def __init__(self, *args, **kwargs):
    # method constructor with arguments

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
    # method magic for print class id and dictionary
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
    # method updates the updated_at with the current datetime
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
    # returns a dictionary containing all keys/values of __dict__ of the instance
        d = dict(self.__dict__)
        d["__class__"] = type(self).__name__
        d["created_at"] = d["created_at"].isoformat()  
        d["updated_at"] = d["updated_at"].isoformat()  
        return d
