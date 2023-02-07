#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
=======
"""
Contains definition of the class BaseGeometry
"""


class BaseGeometry():
    """Definition of class BaseGeometry"""

    def area(self):
        """Definition of area method.
           Raises an Exception with message 'area() is not implemented'"""
>>>>>>> 5b415aa45b6b3aae46cf0e94a0553789b46d83d0
        raise Exception("area() is not implemented")
