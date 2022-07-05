#!/usr/bin/python3
""" Module providing a class Student based on 9-student.py
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

    def to_json(self, attrs=None):
        """
        Returns the description - list, dictionary, string,
        integer and boolean

        If attrs is a list of strings,
        only attribute names contained in this list must be retrieved.
        """
        if isinstance(attrs, list) and all(
                map(lambda s: isinstance(s, str), attrs)
        ):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__
