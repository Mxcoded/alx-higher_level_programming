#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
=======
"""
Contains definition of class MyInt
"""


class MyInt(int):
    """Definition of class MyInt that inherits from class int"""

    def __eq__(self, other):
        """Overrides equals, inverting it"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overrides not-equals, inverting it"""
        return int(self) == int(other)
>>>>>>> 5b415aa45b6b3aae46cf0e94a0553789b46d83d0
