import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class A_Through_F_Window(Gtk.Window):
    def __init__(self):
        super().__init__(title="A Through F")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image1 = Gtk.Image()
        image1.set_from_file("assets/A.png")
        button_prev = Gtk.Button(label = "Previous")
        button_close = Gtk.Button(label = "Close")
        button_next = Gtk.Button(label = "Next")

        box_main.pack_start(image1, True, True, 0)
        box_main.add(box_buttons)
        box_buttons.pack_start(button_prev, True, True, 0)
        box_buttons.pack_start(button_close, True, True, 0)
        box_buttons.pack_start(button_next, True, True, 0)
        self.add(box_main)