#!/usr/bin/python3
"""
<<<<<<< HEAD
more class base
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Square class
"""


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ instantiation with size """
        self.__size = size
        super().__init__(self.__size, self.__size)
=======
Contains the definition of the class Square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of class Square that inherits from class Rectangle"""

    def __init__(self, size):
        """Initialise an instance of the class Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
>>>>>>> 5b415aa45b6b3aae46cf0e94a0553789b46d83d0
