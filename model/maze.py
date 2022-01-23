from model.maker import *
from model.model import IMaze, MazeTile


class Maze(IMaze):

    def __init__(self, a_width: int, a_height: int, a_maze_maker: IMazeMaker):
        """
        :param a_width:         Width of maze
        :param a_height:        Height of maze.
        :param a_maze_maker:    Maze maker instance to use to generate the maze. Set to None for empty maze.
        """
        self._m_width = a_width
        self._m_height = a_height

        # If maze maker object is provided, make maze using it.
        if a_maze_maker is not None:
            self._m_maze_maker = a_maze_maker
            self._m_maze_maker.make_maze(a_width, a_height)
        else:
            self._m_map = np.ones((a_width, a_height)) * MazeTile.TRAVERSABLE

    def is_traversable(self, x, y) -> bool:
        return MazeTile.TRAVERSABLE == self._m_map[x, y]

    def get_width(self) -> int:
        return self._m_width

    def get_height(self) -> int:
        return self._m_height

    def get(self, x, y) -> MazeTile:
        return self._m_map[x, y]
