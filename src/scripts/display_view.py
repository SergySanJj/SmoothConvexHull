from tkinter import Canvas
from typing import List

from PIL import Image, ImageDraw
from PIL.ImageTk import PhotoImage

from scripts.bezier import draw_bezier
from scripts.display_model import DisplayModel
from scripts.point import Point


class DisplayView:
    def __init__(self, display_model: DisplayModel, canvas: Canvas):
        self.display_model = display_model
        self.canvas = canvas

    def update(self):
        if len(self.display_model.points.list) < 1000:
            self.canvas.delete("all")

            self.display_model.hull.draw_connected(self.canvas)
            draw_bezier(self.display_model.hull, self.canvas)

            centroid = self.display_model.hull.centroid(include_last=False)
            centroid.point_color = "green"
            centroid.draw(self.canvas)

            self.display_model.points.draw(self.canvas)
        else:
            self.large_count_display()

    def large_count_display(self):
        image = Image.new("RGB", (1000, 900), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        for p in self.display_model.points.list:
            # draw.ellipse((p.x - 2, p.y - 2, p.x + 2, p.y + 2), width=4, fill=128)
            draw.point((p.x, p.y), fill=128)
            draw.point((p.x, p.y - 1), fill=128)
            draw.point((p.x, p.y + 1), fill=128)
            draw.point((p.x - 1, p.y), fill=128)
            draw.point((p.x + 1, p.y), fill=128)
        photo = PhotoImage(image=image)
        self.canvas.image = photo
        self.canvas.create_image(0, 0, image=photo, anchor="nw")
