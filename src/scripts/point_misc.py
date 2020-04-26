import math

from scripts.point import Point


def edge_length(point_a: Point, point_b: Point) -> float:
    return math.sqrt((point_b.x - point_a.x) ** 2 + (point_b.y - point_a.y) ** 2)


def orthogonal(vector: Point) -> Point:
    vector_len = math.sqrt(vector.x ** 2 + vector.y ** 2)
    if vector_len < Point.epsilon:
        return Point(1, 1)
    return Point(vector.y / math.sqrt(vector.x ** 2 + vector.y ** 2),
                 -vector.x / math.sqrt(vector.x ** 2 + vector.y ** 2))


def add_vectors(vec1: Point, vec2: Point) -> Point:
    return Point(vec1.x + vec2.x, vec1.y + vec2.y)


def median_vector(vec1: Point, vec2: Point) -> Point:
    return add_vectors(vec1, vec2).multiply_by_constant(0.5)


def create_vector(start_point: Point, end_point: Point) -> Point:
    return Point(end_point.x - start_point.x, end_point.y - start_point.y)
