from scripts.point import Point
from scripts.point_list import PointList
from scripts.point_misc import *


class DisplayModel:
    def __init__(self):
        self.points = PointList()
        self.hull = PointList()

    def update_hull(self):
        self.hull = self.points.convex_hull()

    def move_points(self, offset: Point):
        i = 0
        for p in self.points.list:
            self.points.list[i] = add_vectors(p, offset)
            i += 1
        i = 0
        for p in self.hull.list:
            self.hull.list[i] = add_vectors(p, offset)
            i += 1
