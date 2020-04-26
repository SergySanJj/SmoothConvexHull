from tkinter import *

from scripts.display_model import DisplayModel
from scripts.display_view import DisplayView
from scripts.point import Point
from scripts.point_list import PointList
from scripts.bezier import *
from scripts.point_misc import create_vector


class SmoothConvex(Frame):
    touch_started = False
    drag_origin = Point(0, 0)
    drag_after = 10
    drag_calls = 0

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.parent.title("Smooth Convex")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6,
                             weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5,
                       sticky=E + W + S + N)

        self.canv.bind("<Button 1>", self.on_touch_left)
        self.canv.bind("<ButtonRelease 1>", self.on_touch_end_left)
        self.canv.bind("<B1-Motion>", self.on_drag_left)

        self.canv.bind("<Button 3>", self.on_touch_right)

        color_lab = Label(self, text="Color: ")
        color_lab.grid(row=0, column=0,
                       padx=6)

        self.display_model = DisplayModel()
        self.display_view = DisplayView(self.display_model, self.canv)

    def on_touch_left(self, event):
        self.touch_started = True
        self.drag_origin = Point(event.x, event.y)

    def on_touch_end_left(self, event):
        if self.touch_started:
            self.display_model.points.add(Point(event.x, event.y))
            self.display_model.update_hull()
            self.display_view.update()

            self.touch_started = False
            self.drag_calls = 0

    def on_drag_left(self, event):
        if self.drag_calls > self.drag_after:
            self.touch_started = False
            offset = create_vector(self.drag_origin, Point(event.x, event.y))
            self.display_model.move_points(offset)
            self.display_view.update()
            self.drag_origin = Point(event.x, event.y)
        else:
            self.drag_calls += 1

    def on_touch_right(self, event):
        self.display_model.points.remove_if_touched(event.x, event.y)
        self.display_model.update_hull()
        self.display_view.update()


def main():
    root = Tk()
    root.geometry("900x800")
    app = SmoothConvex(root)
    root.mainloop()
