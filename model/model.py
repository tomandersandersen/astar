class MazeTile:
    """
    Tile class.
    """
    NON_TRAVERSABLE = 0
    TRAVERSABLE = 1


class IMaze:
    """
    Maze world interface class
    """

    def is_traversable(self, x, y) -> bool:
        """
        :return: True if point (x, y) is traversable.
        """
        raise NotImplementedError()

    def get(self, x, y) -> MazeTile:
        """
        :return: Returns the tile type at point (x, y).
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
