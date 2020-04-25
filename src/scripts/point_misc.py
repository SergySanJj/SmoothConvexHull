import math

from scripts.point import Point


def edge_length(point_a: Point, point_b: Point):
    return math.sqrt((point_b.x - point_a.x) ** 2 + (point_b.y - point_a.y) ** 2)
