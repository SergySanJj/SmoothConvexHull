from tkinter import BooleanVar

from .point_list import PointList
from .point_misc import *
import random


class DisplayModel:
    def __init__(self):
        self.points: PointList = PointList()
        self.hull: PointList = PointList()
        self.closeness: float = 3.
        self.current_zoom = 0
        self.show_points: BooleanVar = BooleanVar()
        self.show_points.set(True)
        self.show_hull: BooleanVar = BooleanVar()
        self.show_hull.set(True)
        self.show_bezier: BooleanVar = BooleanVar()
        self.show_bezier.set(True)

    def update_hull(self):
        self.hull = self.points.convex_hull()

    def move_points(self, offset: Point):
        self.points.move_by(offset)
        self.hull.move_by(offset)

    def zoom_points(self, multiplier: float, origin: Point):
        if multiplier > 1:
            change = 1
        else:
            change = -1
        if -4 < self.current_zoom + change < 6:
            self.points.zoom_relative(multiplier, origin)
            self.hull.zoom_relative(multiplier, origin)
            self.current_zoom += change

    def spawn_random_points(self, x0, y0, x1, y1, point_count: int):
        for i in range(0, point_count):
            x = random.uniform(x0, x1)
            y = random.uniform(y0, y1)
            self.points.add(Point(x, y))

        self.update_hull()

    def clear(self):
        self.points = PointList()
        self.hull = PointList()
