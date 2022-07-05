#!/usr/bin/python3
# that serializes instances to a JSON
# file and deserializes JSON file to instances

import json
import os


class FileStorage:
    # class FileStorage

    __file_path = "file.json"
    __objects = {}
    d = {}

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
        new_dic = {}
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            for key, obj in self.__objects.items():
                new_dic[key] = obj
            f.write(json.dumps(new_dic, sort_keys=True, default=str))

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.user import User
        new_dic = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file_json:
                new_dic = json.load(file_json)
                for key, obj in new_dic.items():
                    new_obj = User(obj)
                    self.__objects[key] = new_obj
        else:
            pass