from math import sqrt

from kivy.graphics import Color, Ellipse


class Point:
    epsilon = 1
    diam = 10.

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.dist(point_b=other) < self.epsilon
        return False

    def draw(self, canvas):
        with canvas:
            Color(1, 0, 0)
            Ellipse(pos=(self.x - self.diam / 2, self.y - self.diam / 2), size=(self.diam, self.diam))

    def dist(self, point_b):
        return sqrt((self.x - point_b.x) ** 2 + (self.y - point_b.y) ** 2)

    def is_touched(self, x, y):
        return self.dist(Point(x, y)) < self.diam / 2
