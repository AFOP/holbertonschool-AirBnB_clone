#!/usr/bin/python3
# that serializes instances to a JSON file and deserializes JSON file to instances

import json
import os
from models.base_model import BaseModel

class FileStorage:
    # class FileStorage

    __file_path = "file.json"
    __objects = {} 

    def all(self):
    # returns the dictionary __objects
        return self.__objects

    def new(self, obj):
    # sets in __objects the obj with key <obj class name>.id
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
    # serializes __objects to the JSON file (path: __file_path)
        pass
    
    def reload(self):
    # deserializes the JSON file to __objects
        pass