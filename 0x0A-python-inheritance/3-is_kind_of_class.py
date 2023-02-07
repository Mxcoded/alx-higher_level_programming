#!/usr/bin/python3
<<<<<<< HEAD
''' module: 2-is_same_class
'''


def is_kind_of_class(obj, a_class):
    '''function: is_kind_of_class
    obj: an object
    a_class: a class
    Returns: Bool
    '''
    return isinstance(obj, a_class)
=======
"""
Module for is_same_class method
"""


def is_same_class(obj, a_class):
    """Method for comparing object classes

    Args:
        obj (unknown): object whose type is to be checked.
        a_class (str): class criteria to validate.

    Return:
        True if obj isinstance of a_class/ class that inherits from it.
        otherwise False

    """

    if issubclass(type(obj), a_class) or isinstance(obj, a_class):
        return True
    return False
>>>>>>> 5b415aa45b6b3aae46cf0e94a0553789b46d83d0
