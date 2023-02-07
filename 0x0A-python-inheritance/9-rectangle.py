#!/usr/bin/python3
"""
<<<<<<< HEAD
more class base
"""


=======
Contains definition of class Reactangle that inherits from BaseGeometry.
"""

>>>>>>> 5b415aa45b6b3aae46cf0e94a0553789b46d83d0
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
<<<<<<< HEAD
    """ definition of a Rectangle """
    def __init__(self, width, height):
        """ constructor and width, height"""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """ print """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
=======
    """Defnifition of class Rectangle that inherits from BaseGeometry.
       Attributes:
            width (int): width of the rectangle.
            height (int) height of the rectangle.
    """

    def __init__(self, width, height):
        """Initializes an instance of class Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width

        self.__height = height

    def area(self):
        """Returns are of the rectangle"""

        area = self.__width * self.__height
        return area

    def __str__(self):
        """
        Returns string representation of an instance of class rectangle
        """
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
>>>>>>> 5b415aa45b6b3aae46cf0e94a0553789b46d83d0
