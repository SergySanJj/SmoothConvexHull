from tkinter import Canvas

from scripts.bezier import draw_bezier
from scripts.display_model import DisplayModel


class DisplayView:
    def __init__(self, display_model: DisplayModel, canvas: Canvas):
        self.display_model = display_model
        self.canvas = canvas

    def update(self):
        self.canvas.delete("all")

        self.display_model.points.draw(self.canvas)
        self.display_model.hull.draw_connected(self.canvas)
        draw_bezier(self.display_model.hull, self.canvas)

        centroid = self.display_model.hull.centroid(include_last=False)
        centroid.point_color = "green"
        centroid.draw(self.canvas)