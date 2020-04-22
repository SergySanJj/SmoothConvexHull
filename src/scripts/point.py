from math import sqrt

from kivy.graphics import Color, Ellipse


class Point:
    epsilon = 0.00001

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
            d = 10.
            Ellipse(pos=(self.x - d / 2, self.y - d / 2), size=(d, d))

    def dist(self, point_b):
        return sqrt((self.x - point_b.x) ** 2 + (self.y - point_b.y) ** 2)
