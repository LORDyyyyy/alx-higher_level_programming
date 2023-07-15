#!/use/bin/python3
"""here goes everything"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Sqaure class"""

    def __init__(self, size, x=0, y=0, id=None):
        """init"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Return private attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Set private attribute
        """
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """updates the values"""

        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    self.__setattr__(key, value)
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
    def to_dictionary(self):
        """save as dict"""

        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
