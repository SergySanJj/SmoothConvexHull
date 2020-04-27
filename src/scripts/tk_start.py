from tkinter import *

from scripts.display_model import DisplayModel
from scripts.display_view import DisplayView
from scripts.point import Point
from scripts.point_list import PointList
from scripts.bezier import *
from scripts.point_misc import create_vector

from PIL import Image, ImageDraw


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

        self.parent.bind("<MouseWheel>", self.on_mouse_wheel)

        self.display_model = DisplayModel()
        self.display_view = DisplayView(self.display_model, self.canv)

        spawn_button = Button(self, text="Spawn N points", command=self.on_spawn_button)
        spawn_button.grid(row=0, column=1, padx=6, pady=6)
        self.spawn_count: Entry = Entry(self, textvariable=str(100))
        self.spawn_count.grid(row=0, column=2, padx=6, pady=6)
        self.spawn_count.delete(0, END)
        self.spawn_count.insert(0, str(100))

        spawn_button = Button(self, text="Clear", command=self.on_clear)
        spawn_button.grid(row=1, column=1, padx=6, pady=6)

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
            self.drag_origin = Point(event.x, event.y)

    def on_touch_right(self, event):
        self.display_model.points.remove_if_touched(event.x, event.y)
        self.display_model.update_hull()
        self.display_view.update()

    def on_mouse_wheel(self, event):
        delta = event.delta
        if delta > 0:
            multiplier = 2
        else:
            multiplier = 1. / 2.
        self.display_model.zoom_points(multiplier, Point(event.x, event.y))
        self.display_view.update()
        self.display_view.update()

    def on_spawn_button(self):
        try:
            n = int(self.spawn_count.get())
        except ValueError:
            n = 0
        self.display_model.spawn_random_points(100, 100, 800, 800, n)
        self.display_view.update()

    def on_clear(self):
        self.display_model.clear()
        self.display_view.update()


def main():
    root = Tk()
    root.geometry("1000x900")
    root.resizable(False, False)
    app = SmoothConvex(root)

    root.mainloop()
