import unittest

from model.maze import *


class TestMyMaze(unittest.TestCase):

    def test_maze_api(self):
        w = 13
        h = 26
        maze = Maze(w, h, None)

        self.assertEqual(maze.get_width(), w)
        self.assertEqual(maze.get_height(), h)

        # Assert all tiles are traversable (default behaviour).
        for x in range(w):
            for y in range(h):
                self.assertTrue(maze.is_traversable(x, y))

