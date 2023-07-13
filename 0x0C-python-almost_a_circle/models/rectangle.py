#!/usr/bin/python3
"""A script that defines a subclass of Base class"""
from models.base import Base


class Rectangle(Base):
    """A subclass of the superclass Base
        properties
            getter methods: it retrieves the instance attributes
            setter methods: it sets the instance attributes
        attributes
            height: private instance attribute which represents the height of
                the rectangle
            width : private instance attribute. It represents the width of
                rectangle
            x: a private instance attribute
            y: a private instance attribute
        constructor: initialises an instance of the Rectangle class
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("the value is not a number")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("the value is not a number")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("the value is not a number")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("the value is not a number")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")
        else:
            self.__width = width
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")
        else:
            self.__height = height
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        else:
            self.__x = x
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")
        else:
            self.__y = y
