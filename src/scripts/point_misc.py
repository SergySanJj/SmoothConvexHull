import math

from scripts.point import Point


def edge_length(point_a: Point, point_b: Point) -> float:
    return math.sqrt((point_b.x - point_a.x) ** 2 + (point_b.y - point_a.y) ** 2)


def orthogonal(vector: Point) -> Point:
    return Point(vector.y / math.sqrt(vector.x ** 2 + vector.y ** 2),
                 -vector.x / math.sqrt(vector.x ** 2 + vector.y ** 2))


def add_vectors(vec1: Point, vec2: Point) -> Point:
    return Point(vec1.x + vec2.x, vec1.y + vec2.y)


def median_vector(vec1: Point, vec2: Point) -> Point:
    return add_vectors(vec1, vec2).multiply_by_constant(0.5)
