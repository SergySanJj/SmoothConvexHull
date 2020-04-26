import math

from scripts.point import Point


def edge_length(point_a: Point, point_b: Point):
    return math.sqrt((point_b.x - point_a.x) ** 2 + (point_b.y - point_a.y) ** 2)


def orthogonal(vector: Point) -> Point:
    return Point(vector.y / math.sqrt(vector.x ** 2 + vector.y ** 2),
                 -vector.x / math.sqrt(vector.x ** 2 + vector.y ** 2))


def add_vectors(vec1: Point, vec2: Point):
    return Point(vec1.x + vec2.x, vec1.y + vec2.y)
