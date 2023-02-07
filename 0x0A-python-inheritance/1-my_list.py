#!/usr/bin/python3
<<<<<<< HEAD
''' Module: 1-my_list
'''


class MyList(list):
    ''' Represents a MyList
    '''

    def print_sorted(self):
        '''
        prints the list, but sorted
        '''
        print(sorted(self))
=======
"""
Contains definiton for the class MyList that inherits from list.
"""


class MyList(list):
    """definiton for the class MyList that inherits from list.
    """
    def print_sorted(self):
        """Prints list elements(int) in ascending order"""

        sortedlist = sorted(self)
        print(sortedlist)
>>>>>>> 5b415aa45b6b3aae46cf0e94a0553789b46d83d0
