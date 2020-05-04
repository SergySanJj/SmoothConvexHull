import math

from .point import Point
from .point_list import PointList
from tkinter import Canvas, W

from .point_misc import edge_length, orthogonal, add_vectors, median_vector


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

    # last segment might not be present in loop
    draw_points.append(p3.x)
    draw_points.append(p3.y)

    canvas.create_line(draw_points, width=2, fill='darkgreen')


def smooth_cubic(start_point: Point, end_point: Point, canvas: Canvas, median_start: Point, median_end: Point,
                 multiplier=30.):
    normal_start = orthogonal(median_start).normalize().multiply_by_constant(-multiplier)
    normal_end = orthogonal(median_end).normalize().multiply_by_constant(multiplier)

    smooth1 = add_vectors(start_point, normal_start)
    smooth2 = add_vectors(end_point, normal_end)

    smooth1.point_color = "mediumseagreen"
    smooth2.point_color = "mediumseagreen"
    smooth1.outline_color = 'black'
    smooth2.outline_color = 'black'
    smooth1.diam = 6
    smooth2.diam = 6

    bezier_cubic(start_point, smooth1, smooth2, end_point, canvas)

    draw_connection(start_point, smooth1, canvas)
    draw_connection(end_point, smooth2, canvas)

    smooth1.draw(canvas)
    smooth2.draw(canvas)


def draw_bezier(points: PointList, canvas: Canvas, closeness: float = 3.):
    if len(points.list) > 2:
        curr = 0
        while curr + 1 < len(points.list):
            start_point = points.list[curr]
            end_point = points.list[curr + 1]

            if curr == 0:
                prev_point = points.list[curr - 2]
            else:
                prev_point = points.list[curr - 1]

            if curr + 2 < len(points.list):
                next_point = points.list[curr + 2]
            else:
                next_point = points.list[1]

            median_start = median_vector(Point(start_point.x - prev_point.x,
                                               start_point.y - prev_point.y).normalize(),
                                         Point(start_point.x - end_point.x,
                                               start_point.y - end_point.y).normalize()).normalize()
            median_end = median_vector(Point(end_point.x - start_point.x, end_point.y - start_point.y).normalize(),
                                       Point(end_point.x - next_point.x,
                                             end_point.y - next_point.y).normalize()).normalize()

            draw_ray(start_point, median_start, canvas)
            draw_ray(end_point, median_end, canvas)

            smooth_cubic(start_point, end_point, canvas, median_start, median_end,
                         edge_length(start_point, end_point) / closeness)
            curr += 1


def draw_ray(start_point: Point, direction_vector: Point, canvas: Canvas):
    end_point = add_vectors(start_point, direction_vector.multiply_by_constant(100))
    canvas.create_line(start_point.x, start_point.y,
                       end_point.x, end_point.y, fill='grey90')


def draw_connection(start_point: Point, end_point: Point, canvas: Canvas):
    canvas.create_line(start_point.x, start_point.y,
                       end_point.x, end_point.y,
                       width=3, fill='black')
    canvas.create_line(start_point.x, start_point.y,
                       end_point.x, end_point.y,
                       width=1, fill='pink')
