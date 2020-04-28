from tkinter import Canvas
from typing import List

from PIL import Image, ImageDraw
from PIL.ImageTk import PhotoImage

from scripts.bezier import draw_bezier
from scripts.display_model import DisplayModel
from scripts.point import Point


class DisplayView:
    def __init__(self, display_model: DisplayModel, canvas: Canvas):
        self.display_model: DisplayModel = display_model
        self.canvas: Canvas = canvas

    def update(self):
        self.canvas.delete("all")
        if len(self.display_model.points.list) < 1000:
            if self.display_model.show_hull.get():
                self.display_model.hull.draw_connected(self.canvas)
            if self.display_model.show_bezier.get():
                draw_bezier(self.display_model.hull, self.canvas, self.display_model.blobness)

            centroid = self.display_model.hull.centroid(include_last=False)
            centroid.point_color = "green"
            centroid.draw(self.canvas)
            if self.display_model.show_points.get():
                self.display_model.points.draw(self.canvas)
        else:
            self.large_count_display()

    def large_count_display(self):
        image = Image.new("RGB", (1000, 900), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        if self.display_model.show_points.get():
            for p in self.display_model.points.list:
                draw.point((p.x, p.y), fill=128)
        if self.display_model.show_hull.get():
            hull_polygon = []
            for p in self.display_model.hull.list:
                hull_polygon.append((p.x, p.y))
            draw.line(hull_polygon, '#D3D3D3', 3)

        photo = PhotoImage(image=image)
        self.canvas.image = photo
        self.canvas.create_image(0, 0, image=photo, anchor="nw")

        if self.display_model.show_bezier.get():
            draw_bezier(self.display_model.hull, self.canvas, self.display_model.blobness)
