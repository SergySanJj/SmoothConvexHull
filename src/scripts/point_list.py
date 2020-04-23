from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.uix.label import Label

from scripts.point import Point


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
        with canvas:
            i = 0
            for p in self.list:
                print(i)
                Label(center_x=p.x + 10, center_y=p.y + 5, text=str(i), outline_color=[0, 0, 0], font_size=25,
                      outline_width=1)
                i += 1


    def draw_connected(self, canvas):
        with canvas:
            Color(0., 0., 0.)
            points = []
            for p in self.list:
                points.append(p.x)
                points.append(p.y)
            if len(self.list) > 0:
                points.append(self.list[0].x)
                points.append(self.list[0].y)
            Line(points=points)



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
        tmp = sorted(self.list, key=lambda point: point.slope(center))
        tmp.append(tmp[0])

        def cross_product_orientation(a, b, c):
            return (b.y - a.y) * \
                   (c.x - a.x) - \
                   (b.x - a.x) * \
                   (c.y - a.y)

        # convex_hull is a stack of points beginning with the leftmost point.
        for p in tmp:
            # if we turn clockwise to reach this point, pop the last point from the stack, else, append this point to it.
            while len(hull.list) > 1 and cross_product_orientation(hull.list[-2], hull.list[-1], p) >= 0:
                hull.list.pop()
            hull.list.append(p)
        # the stack is now a representation of the convex hull, return it.
        return hull

    def print(self):
        print(self.list)
