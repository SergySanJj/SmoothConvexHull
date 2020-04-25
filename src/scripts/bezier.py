import math

from scripts.point import Point
from scripts.point_list import PointList
from tkinter import Canvas, W


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
    while t < 1.:
        x = (1 - t) ** 3 * p0.x + \
            (1 - t) ** 2 * 3 * t * p1.x + \
            (1 - t) * 3 * t * t * p2.x + \
            t ** 3 * p3.x
        y = (1 - t) ** 3 * p0.y + \
            (1 - t) ** 2 * 3 * t * p1.y + \
            (1 - t) * 3 * t * t * p2.y + \
            t ** 3 * p3.y

        canvas.create_oval(x, y, x, y, width=2, fill='green')

        t += scale


def smooth_cubic(start_point: Point, end_point: Point, canvas: Canvas):
    dx = end_point.x - start_point.x
    dy = end_point.y - start_point.y
    smooth1 = Point(start_point.x + dx / 3., start_point.y + dy / 3.)
    smooth2 = Point(start_point.x + 2 * dx / 3., start_point.y + 2 * dy / 3.)

    orthx = dy / math.sqrt(dx ** 2 + dy ** 2)
    orthy = -dx / math.sqrt(dx ** 2 + dy ** 2)
    smooth1.x += orthx * 100
    smooth1.y += orthy * 100

    smooth2.x += orthx * 100
    smooth2.y += orthy * 100

    smooth1.point_color = "pink"
    smooth2.point_color = "pink"
    smooth1.draw(canvas)
    smooth2.draw(canvas)
    bezier_cubic(start_point, smooth1, smooth2, end_point, canvas)


def draw_bezier(points: PointList, canvas: Canvas):
    center = points.centroid()
    if len(points.list) > 2:
        # first pair

        curr = 0
        while curr + 1 < len(points.list):
            start_point = points.list[curr]
            end_point = points.list[curr + 1]
            smooth_cubic(start_point, end_point, canvas)
            curr += 1
