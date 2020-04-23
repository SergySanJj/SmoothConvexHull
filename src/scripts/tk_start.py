from tkinter import *

from scripts.point import Point
from scripts.point_list import PointList


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
        self.canv.create_rectangle(0, 0, self.canv.winfo_width(), self.canv.winfo_height(), fill="white")
        centroid = self.points.centroid()
        centroid.point_color = "green"
        centroid.draw(self.canv)

        self.points.draw(self.canv)
        hull = self.points.convex_hull()
        print("hull size", ["{" + str(p.x) + " " + str(p.y) + "}" for p in hull.list])
        hull.draw_connected(self.canv)


def main():
    root = Tk()
    root.geometry("800x600")
    app = SmoothConvex(root)
    root.mainloop()
