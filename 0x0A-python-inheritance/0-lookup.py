#!/usr/bin/python3

''' function that returns the list
'''


def lookup(obj):
    ''' function: lookup()
    Returns a list object
    '''
    return dir(obj)


"""
Contains definition of the function lookup
"""


def lookup(obj):
    """Returns list of attributes and methods of an object

    Args:
        obj (any): object whose attributes and methods are to be returned

    """

    return (dir(obj))
