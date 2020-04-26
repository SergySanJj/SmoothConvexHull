import math

from scripts.point import Point
from scripts.point_list import PointList
from tkinter import Canvas, W

from scripts.point_misc import edge_length, orthogonal, add_vectors


def bezier_quad(p0: Point, p1: Point, p2: Point, canvas: Canvas, scale=0.01):
    t = 0.0
    while t < 1.:
        x = (1. - t) ** 2 * p0.x + \
            (1. - t) * 2 * t * p1.x \
            + t ** 2 * p2.x
        y = (1. - t) ** 2 * p0.y + \
            (1. - t) * 2 * t * p1.y \
            + t ** 2 * p2.y

        canvas.create_oval(x, y, x, y, width=2, fill='green')

        t += scale


def bezier_cubic(p0: Point, p1: Point, p2: Point, p3: Point, canvas: Canvas, scale=0.01):
    t = 0.0
    draw_points = []
    while t < 1.:
        x = (1 - t) ** 3 * p0.x + \
            (1 - t) ** 2 * 3 * t * p1.x + \
            (1 - t) * 3 * t * t * p2.x + \
            t ** 3 * p3.x
        y = (1 - t) ** 3 * p0.y + \
            (1 - t) ** 2 * 3 * t * p1.y + \
            (1 - t) * 3 * t * t * p2.y + \
            t ** 3 * p3.y

        # canvas.create_oval(x, y, x, y, width=2, fill='green')
        draw_points.append(x)
        draw_points.append(y)

        t += scale
    canvas.create_line(draw_points, fill='violet')


def smooth_cubic(start_point: Point, end_point: Point, canvas: Canvas, center: Point, multiplier=30):
    central_to_start = Point(start_point.x - center.x, start_point.y - center.y)
    central_to_end = Point(end_point.x - center.x, end_point.y - center.y)

    normal_start = orthogonal(central_to_start).normalize().multiply_by_constant(-multiplier)
    normal_end = orthogonal(central_to_end).normalize().multiply_by_constant(multiplier)

    smooth1 = add_vectors(start_point, normal_start)
    smooth2 = add_vectors(end_point, normal_end)

    smooth1.point_color = "pink"
    smooth2.point_color = "pink"
    smooth1.draw(canvas)
    smooth2.draw(canvas)
    bezier_cubic(start_point, smooth1, smooth2, end_point, canvas)


def draw_bezier(points: PointList, canvas: Canvas):
    center = points.centroid()
    avg_len = points.avg_edge_length()
    if len(points.list) > 2:
        curr = 0
        while curr + 1 < len(points.list):
            start_point = points.list[curr]
            end_point = points.list[curr + 1]
            smooth_cubic(start_point, end_point, canvas, center, 50 * edge_length(start_point, end_point) / avg_len)
            curr += 1
