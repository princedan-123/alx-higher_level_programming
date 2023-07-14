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
            x: a private instance attribute for horizontal positioning of the
                square
            y: a private instance attribute for vertical positioning
            area: a method that calculates the area of the rectangle
            display: gives a visual display of the rectangle using #
            update: a variadic method that updates the instance attributes
        constructor: initialises an instance of the Rectangle class
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def area(self):
        return self.width * self.height

    def display(self):
        if self.x == 0 and self.y == 0:
            for i in range(self.height):
                print("#" * self.width)
        elif self.x > 0 or self.y > 0:
            space = " " * self.x
            breadth = "#" * self.width
            for i in range(self.y):
                print()
            for i in range(self.height):
                print(space + breadth)

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            list_length = len(args)
            self.id = args[0]
            i = 1
            while i < list_length:
                if i == 1:
                    if not isinstance(args[1], int):
                        raise TypeError("width must be an integer")
                    if args[1] <= 0:
                        raise ValueError("width must be > 0")
                    self.__width =  args[1]
                if i == 2:
                    if not isinstance(args[2], int):
                        raise TypeError("height must be an integer")
                    if args[2] <= 0:
                        raise ValueError("height must be > 0")
                    self.__height = args[2]
                if i == 3:
                    if not isinstance(args[3], int):
                        raise TypeError("x must be an integer")
                    if args[3] < 0:
                        raise ValueError("x must be >= 0")
                    self.__x = args[3]
                if i == 4:
                    if not isinstance(args[4], int):
                        raise TypeError("y must be an integer")
                    if args[4] < 0:
                        raise ValueError("y must be >= 0")
                    self.__y = args[4]
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    if not isinstance(value, int):
                        raise TypeError("id is not an integer")
                    self.id = value
                if key == "width":
                    if not isinstance(value, int):
                        raise TypeError("width must be an integer")
                    if value <= 0:
                        raise ValueError("width must be > 0")
                    self.__width = value
                if key == "height":
                    if not isinstance(value, int):
                        raise TypeError("height must be an integer")
                    if value <= 0:
                        raise ValueError("height must be > 0")
                    self.__height = value
                if key == "x":
                    if not isinstance(value, int):
                        raise TypeError("x must be an integer")
                    if value < 0:
                        raise ValueError("x must be >= 0")
                    self.__x = value
                if key == "y":
                    if not isinstance(value, int):
                        raise TypeError("y must be an integer")
                    if value < 0:
                        raise ValueError("y must be >= 0")
                    self.__y = value
