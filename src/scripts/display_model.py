from scripts.point import Point
from scripts.point_list import PointList
from scripts.point_misc import *
import random


class DisplayModel:
    def __init__(self):
        self.points = PointList()
        self.hull = PointList()

    def update_hull(self):
        self.hull = self.points.convex_hull()

    def move_points(self, offset: Point):
        self.points.move_by(offset)
        self.hull.move_by(offset)

    def zoom_points(self, multiplier: float, origin: Point):
        self.points.zoom_relative(multiplier, origin)
        self.hull.zoom_relative(multiplier, origin)

    def spawn_random_points(self, x0, y0, x1, y1, point_count: int):
        for i in range(0, point_count):
            x = random.uniform(x0, x1)
            y = random.uniform(y0, y1)
            self.points.add(Point(x, y))

        self.update_hull()
