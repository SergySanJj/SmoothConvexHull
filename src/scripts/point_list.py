import math
from tkinter import Canvas, W

from scripts.point import Point
from scripts.point_misc import edge_length


class PointList:
    def __init__(self):
        self.list = []

    def add(self, new_point: Point):
        self.list.append(new_point)

    def remove(self, point_to_remove: Point):
        self.list = [p for p in self.list if point_to_remove.dist(p) > Point.epsilon]

    def remove_if_touched(self, x, y):
        self.list = [p for p in self.list if not p.is_touched(x, y)]

    def exists(self, point: Point) -> bool:
        for p in self.list:
            if point.dist(p) < Point.epsilon:
                return True
        return False

    def draw(self, canvas):
        for p in self.list:
            p.draw(canvas)

    def draw_connected(self, canvas: Canvas):
        if len(self.list) > 0:
            points = []
            for p in self.list:
                points.append(p.x)
                points.append(p.y)

            canvas.create_line(points, fill="black")

            i = 0
            for p in self.list:
                canvas.create_text(p.x + 10, p.y + 10, anchor=W, font="Arial",
                                   text=str(i), fill='blue')
                i += 1

    def sort(self, cmp=lambda point: point.x):
        self.list = sorted(self.list, key=cmp)

    def centroid(self) -> Point:
        if len(self.list) == 0:
            return Point(0., 0.)
        x = 0
        y = 0
        for p in self.list:
            x += p.x
            y += p.y
        x = x / len(self.list)
        y = y / len(self.list)
        return Point(x, y)

    def convex_hull(self):
        hull = PointList()
        if len(self.list) == 0:
            return hull
        center = self.centroid()
        tmp = self.list
        left_most = self.left_most_pos()
        tmp[0], tmp[left_most] = tmp[left_most], tmp[0]
        tmp = tmp[:1] + sorted(tmp[1:], key=lambda point: point.polar_angle(tmp[0]))

        def cross_product_orientation(a: Point, b: Point, c: Point):
            return (b.y - a.y) * \
                   (c.x - a.x) - \
                   (b.x - a.x) * \
                   (c.y - a.y)

        for p in tmp:
            while len(hull.list) > 1 and cross_product_orientation(hull.list[-2], hull.list[-1], p) >= 0:
                hull.list.pop()
            hull.list.append(p)

        hull.list.append(hull.list[0])

        return hull

    def left_most_pos(self) -> int:
        pos = 0
        i = 0
        for p in self.list:
            if p.x < self.list[pos].x:
                pos = i
            i += 1
        return pos

    def print(self):
        print(["{" + str(p.x) + " " + str(p.y) + "}" for p in self.list])

    def avg_edge_length(self):
        avg = 0.
        i = 0
        while i < len(self.list) - 1:
            avg += edge_length(self.list[i], self.list[i + 1])
            i += 1

        avg = avg / (len(self.list) - 1)
        return avg
