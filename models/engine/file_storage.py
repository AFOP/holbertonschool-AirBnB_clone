#!/usr/bin/python3
# that serializes instances to a JSON
# file and deserializes JSON file to instances

import json
import os


class FileStorage:
    # class FileStorage

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            self.__objects = json.dumps(
                self.__objects, sort_keys=True, default=str)
            f.write(self.__objects)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file_json:
                self.__objects = json.loads(file_json.read())
        else:
            pass
