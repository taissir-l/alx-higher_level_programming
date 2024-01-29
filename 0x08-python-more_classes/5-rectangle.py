#!/usr/bin/python3
"""class of a rectangle"""


class Rectangle:
    """initialise a rectangle"""

    def __init__(self, width=0, height=0):
        """rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError: size is not integer
            ValueError: size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gives width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gives height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """message for the object that is deleted"""
        print("Bye rectangle...")
