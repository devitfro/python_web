import json
from protocols.serializable import Serializable


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def serialize(self):
        return json.dumps(self.__dict__)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def serialize(self):
        return json.dumps(self.__dict__)


def serialize_object(obj: Serializable):
    return obj.serialize()