#!/usr/bin/python3
"""this script creates a subclass called square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A subclass that inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """retrieves the width attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size attributes"""
        self.width = value
        self.height = value
