"""
Maze world interface class
"""


class IMaze:

    def is_traversable(self, x, y) -> bool:
        """
        :return: True if point (x, y) is traversable.
        """
        raise NotImplementedError()

    def get_width(self) -> int:
        """
        :return: Returns the width of the map.
        """
        raise NotImplementedError()

    def get_height(self) -> int:
        """
        :return: Returns the height of the map.
        """
        raise NotImplementedError()
