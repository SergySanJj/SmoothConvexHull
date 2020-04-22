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
