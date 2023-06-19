#!/usr/bin/python3

"""Contains the Square Class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor
        """

        super().__init__(width=size, height=size, x=x, y=y, id=id)



    def __str__(self):
        """provides output for str() and print()
        """

        return "[Square] ({}) {}/{} - {}".format(self.id, self._Rectangle__x,
                                                 self._Rectangle__y,
                                                 self._Rectangle__width)

    def update(self, *args, **kwargs):
        """updates the instance attributes

        function will skip over **kwargs if *args exists and is not empty
        """

        if len(args) <= 0:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = kwargs["size"]
                    self.height = kwargs["size"]
                elif key == "height":
                    self.height = kwargs["height"]
                elif key == "width":
                    self.width = kwargs["width"]
                elif key == "id":
                    self.id = kwargs["id"]
                elif key == "x":
                    self.x = kwargs["x"]
                elif key == "y":
                    self.y = kwargs["y"]

            return

        if len(args) > 0:
            self.id = args[0]

        if len(args) > 1:
            self.width = args[1]
            self.height = args[1]

        if len(args) > 2:
            self.x = args[2]

        if len(args) > 3:
            self.y = args[3]
