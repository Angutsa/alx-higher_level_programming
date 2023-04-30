#!/usr/bin/python3

"""Contains the Student Class
"""


class Student:
    """Defines a student
    """

    def __init__(self, first_name, last_name, age):
        """Initialises the object

        Attributes:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student in years
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): list of attributes to retrieve.

        Description:
            If 'attrs' is not present, the method returns all the attributes
        """

        attributes = self.__dict__

        if attrs is None:
            return attributes

        attribs = {}
        for attr in attrs:
            try:
                attribs[attr] = attributes[attr]
            except KeyError:
                continue

        return attribs
