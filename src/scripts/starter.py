from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from scripts.point_list import PointList
from scripts.point import Point

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class PointWidget(Widget):

    points = PointList()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def on_touch_down(self, touch):
        if touch.button == 'left':
            print("left mouse clicked")
            self.points.add(Point(touch.x, touch.y))
            self.redraw()
        if touch.button == 'right':
            print("right mouse clicked")
            self.points.remove_if_touched(touch.x, touch.y)
            self.redraw()

    def redraw(self):
        with self.canvas:
            Color(1., 1., 1.)
            Rectangle(pos=(0, 0), size=self.size)
        self.points.draw(self.canvas)


class SmoothConvexApp(App):
    draw_widget = PointWidget()

    def on_start(self):
        self.draw_widget.redraw()

    def build(self):
        return self.draw_widget


def main():
    SmoothConvexApp().run()
