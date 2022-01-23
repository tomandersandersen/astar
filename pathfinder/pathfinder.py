from model.model import IMaze


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Path:
    def __init__(self):
        self.path = []


class IPathFinder:

    def find_path(self, maze: IMaze, start: Point, end: Point) -> Path:
        raise NotImplementedError
