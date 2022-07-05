#!/usr/bin/python3
""" Module providing a class Student
"""


class Student:
    """Represents a student.
    """
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the description - list, dictionary, string,
        integer and boolean
        """
        return self.__dict__
