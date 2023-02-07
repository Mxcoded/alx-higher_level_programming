#!/usr/bin/python3
<<<<<<< HEAD
# 2-is_same_class.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
=======
"""
Module for is_same_class method
"""


def is_same_class(obj, a_class):
    """Determines if an object is exactly an instance of a class.

    Args:
        obj (unknown): object whose type is to be checked.
        a_class (str): class criteria to validate.

    """

>>>>>>> 5b415aa45b6b3aae46cf0e94a0553789b46d83d0
    if type(obj) == a_class:
        return True
    return False
