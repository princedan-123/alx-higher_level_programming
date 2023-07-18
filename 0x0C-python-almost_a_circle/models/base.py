#!/usr/bin/python3
"""A script that creates a class"""
import json


class Base:
    """A class called Base that will manage id attribute in future classes
    atrributes
        __nb_objects
        constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """A constructor that initialises an object
            arguments
                id:(int) an integer value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        classname = cls.__name__
        extension = ".json"
        filename = classname + extension
        if not list_objs or len(list_objs) == 0:
            list_objs = []
        content = cls.to_json_string([i.to_dictionary() for i in list_objs])
        with open(filename, "w") as f:
            f.write(content)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            content = list(json.loads(json_string))
            return content

    @classmethod
    def create(cls, **dictionary):
        class_name = cls.__name__
        if class_name == "Rectangle":
            obj = cls(id=0, width=1, height=1, x=0, y=0)
        if class_name == "Square":
            obj = cls(id=0, size=0, x=0, y=0)
        return obj.update(**dictionary)

    @classmethod
    def load_from_file(cls):
        """creates a list of objects from json strings stored in a file"""
        class_name = cls.__name__
        extension = ".json"
        file_name = class_name + extension
        try:
            with open(filename, "r") as f:
                content = f.read()
                dic = cls.from_json_string(content)
                new_objs = [cls.create(**i) for i in dic]
        except FileNotFoundError:
            return []
        except Exception:
            return []
