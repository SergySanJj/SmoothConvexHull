import math
from math import sqrt
from tkinter import Canvas


class Point:
    epsilon = 0.1
    diam = 10.
    point_color = "red"

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.dist(point_b=other) < self.epsilon
        return False

    def draw(self, canvas: Canvas):
        canvas.create_oval(self.x - self.diam / 2, self.y - self.diam / 2, self.x + self.diam / 2,
                           self.y + self.diam / 2, fill=self.point_color,
                           width=2)

    def dist(self, point_b):
        return sqrt((self.x - point_b.x) ** 2 + (self.y - point_b.y) ** 2)

    def is_touched(self, x, y):
        return self.dist(Point(x, y)) < self.diam / 2

    def polar_angle(self, origin):
        dx = self.x - origin.x
        dy = self.y - origin.y
        th = math.atan2(dy, dx)
        return th
