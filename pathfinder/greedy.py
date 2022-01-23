import sys
from typing import List, Tuple

from model.model import IMaze
from pathfinder.pathfinder import IPathFinder, Point, Path


class GreedyPathfinder(IPathFinder):

    def find_path(self, a_maze: IMaze, start: Point, end: Point) -> Path:
        # Set with <score, Point>
        open_set = []
        path = Path()
        current_point = start

        while True:
            neigh_points = self._get_neighbours(a_maze, current_point)

            # For each new point, calculate score and add to open set.
            for p in neigh_points:
                open_set.append((self._manhattan_distance(p, end), p))

            # Find the point with best score (i.e. lowest score).

        return path

    def _min_index(self, open_set: List[Tuple[int, Point]]) -> Tuple[int, float]:
        min_score = sys.maxsize
        min_index = -1
        for index, p in enumerate(open_set):
            score = p[0]
            if score < min_score:
                min_score = score
                min_index = index
        return min_index, min_score

    def _get_neighbours(self, maze: IMaze, point: Point) -> List[Point]:
        neighbour_list = []
        for dx in range(3):
            for dy in range(3):
                if dx is not 0 and dy is not 0:
                    if maze.is_traversable(point.x + dx, point.y + dy):
                        neighbour_list.append(Point(point.x + dx, point.y + dy))
        return neighbour_list

    def _manhattan_distance(self, start: Point, stop: Point) -> float:
        return abs(start.x - stop.x) + abs(start.y - stop.y)
