#!/usr/bin/python3
<<<<<<< HEAD
''' module: 4-inherits_from
'''


def inherits_from(obj, a_class):
    '''the object is an instance of a class that inherited (directly or indirectly)
    obj: an object
    a_class: a class
    returns None
    '''
    return type(obj) != a_class and isinstance(obj, a_class)
=======
"""
Module for is_same_class method
"""


def inherits_from(obj, a_class):
    """Method for comparing object classes

    Args:
        obj (unknown): object whose type is to be checked.
        a_class (str): class criteria to validate.

    Return:
        True if obj isinstance of a_class/ class that inherits from it.
        otherwise False

    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
>>>>>>> 5b415aa45b6b3aae46cf0e94a0553789b46d83d0
