#!/usr/bin/python3
"""
Creates a Square class with size and position attributes.
"""


class Square:
    """
    Square class defined.

    Attributes:
        size (int): Represents the size of the square.
        position (tuple): Represents the position of the square in 2D space.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square object.

        Args:
            size (int): Represents the size of the square.
            position (tuple): Represents the pos square in 2D space.

        Returns:
            None
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): Represents the size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
            tuple: Represents the position of the square in 2D space.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Args:
            value (tuple): Represents the position of the square in 2D space.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.

        Returns:
            None
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a square based on its size and position.

        Returns:
            None
        """
        if self.size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
