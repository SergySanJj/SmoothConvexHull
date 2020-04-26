from tkinter import *

from scripts.point import Point
from scripts.point_list import PointList
from scripts.bezier import *


class SmoothConvex(Frame):
    points = PointList()

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.setUI()

        self.brush_size = 10
        self.brush_color = "black"

    def setUI(self):
        self.parent.title("Smooth Convex")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6,
                             weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5,
                       sticky=E + W + S + N)

        self.canv.bind("<Button-1>", self.on_touch_left)
        self.canv.bind("<Button-3>", self.on_touch_right)

        color_lab = Label(self, text="Color: ")
        color_lab.grid(row=0, column=0,
                       padx=6)

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.brush_color, outline=self.brush_color)

    def on_touch_left(self, event):
        self.points.add(Point(event.x, event.y))
        self.redraw()

    def on_touch_right(self, event):
        self.points.remove_if_touched(event.x, event.y)
        self.redraw()

    def redraw(self):
        self.canv.delete("all")

        self.points.draw(self.canv)
        hull = self.points.convex_hull()
        hull.draw_connected(self.canv)
        draw_bezier(hull, self.canv)

        centroid = hull.centroid(include_last=False)
        centroid.point_color = "green"
        centroid.draw(self.canv)

        # Point(500, 500).draw(self.canv)
        # bezier_cubic(Point(500, 500), Point(400, 100), Point(600, 100), Point(500, 500), self.canv, 0.001)


def main():
    root = Tk()
    root.geometry("800x600")
    app = SmoothConvex(root)
    root.mainloop()
