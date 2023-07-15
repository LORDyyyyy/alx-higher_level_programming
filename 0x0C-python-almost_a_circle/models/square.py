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
