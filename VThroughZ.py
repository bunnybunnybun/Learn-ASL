import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

########################################################################

class V_Through_Z_Window_V(Gtk.Window):
    def __init__(self):
        super().__init__(title="V Through Z")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/V.png")
        label = Gtk.Label(label="")
        label.set_line_wrap(True)
        label.set_line_wrap_mode(Gtk.WrapMode.WORD)
        button_prev = Gtk.Button(label = "Previous")
        button_prev.set_size_request(80, 40)
        button_close = Gtk.Button(label = "Close")
        button_close.connect("clicked", self.on_close_clicked)
        button_close.set_size_request(80, 40)
        button_next = Gtk.Button(label = "Next")
        button_next.connect("clicked", self.on_next_clicked)
        button_next.set_size_request(80, 40)

        box_main.pack_start(image, True, True, 0)
        box_main.pack_start(label, True, True, 0)
        box_main.pack_start(box_buttons, False, False, 0)
        box_buttons.pack_start(button_prev, True, True, 0)
        box_buttons.pack_start(button_close, True, True, 0)
        box_buttons.pack_start(button_next, True, True, 0)
        self.add(box_main)

    def on_next_clicked(self, widget):
        self.destroy()
        v_through_z_window_w = V_Through_Z_Window_W()
        v_through_z_window_w.show_all()


    def on_close_clicked(self, widget):
        self.destroy()

###############################################################################

class V_Through_Z_Window_W(Gtk.Window):
    def __init__(self):
        super().__init__(title="V Through Z")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/W.png")
        label = Gtk.Label(label="")
        label.set_line_wrap(True)
        label.set_line_wrap_mode(Gtk.WrapMode.WORD)
        button_prev = Gtk.Button(label = "Previous")
        button_prev.connect("clicked", self.on_prev_clicked)
        button_prev.set_size_request(80, 40)
        button_close = Gtk.Button(label = "Close")
        button_close.connect("clicked", self.on_close_clicked)
        button_close.set_size_request(80, 40)
        button_next = Gtk.Button(label = "Next")
        button_next.connect("clicked", self.on_next_clicked)
        button_next.set_size_request(80, 40)

        box_main.pack_start(image, True, True, 0)
        box_main.pack_start(label, True, True, 0)
        box_main.pack_start(box_buttons, False, False, 0)
        box_buttons.pack_start(button_prev, True, True, 0)
        box_buttons.pack_start(button_close, True, True, 0)
        box_buttons.pack_start(button_next, True, True, 0)
        self.add(box_main)

    def on_prev_clicked(self, widget):
        self.destroy()
        v_through_z_window_v = V_Through_Z_Window_V()
        v_through_z_window_v.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        v_through_z_window_x = V_Through_Z_Window_X()
        v_through_z_window_x.show_all()

###########################################################################

class V_Through_Z_Window_X(Gtk.Window):
    def __init__(self):
        super().__init__(title="V Through Z")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/X.png")
        label = Gtk.Label(label="")
        label.set_line_wrap(True)
        label.set_line_wrap_mode(Gtk.WrapMode.WORD)
        button_prev = Gtk.Button(label = "Previous")
        button_prev.connect("clicked", self.on_prev_clicked)
        button_prev.set_size_request(80, 40)
        button_close = Gtk.Button(label = "Close")
        button_close.connect("clicked", self.on_close_clicked)
        button_close.set_size_request(80, 40)
        button_next = Gtk.Button(label = "Next")
        button_next.connect("clicked", self.on_next_clicked)
        button_next.set_size_request(80, 40)

        box_main.pack_start(image, True, True, 0)
        box_main.pack_start(label, True, True, 0)
        box_main.pack_start(box_buttons, False, False, 0)
        box_buttons.pack_start(button_prev, True, True, 0)
        box_buttons.pack_start(button_close, True, True, 0)
        box_buttons.pack_start(button_next, True, True, 0)
        self.add(box_main)

    def on_prev_clicked(self, widget):
        self.destroy()
        v_through_z_window_w = V_Through_Z_Window_W()
        v_through_z_window_w.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        v_through_z_window_y = V_Through_Z_Window_Y()
        v_through_z_window_y.show_all()

#####################################################################

class V_Through_Z_Window_Y(Gtk.Window):
    def __init__(self):
        super().__init__(title="V Through Z")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/Y.png")
        label = Gtk.Label(label="")
        label.set_line_wrap(True)
        label.set_line_wrap_mode(Gtk.WrapMode.WORD)
        button_prev = Gtk.Button(label = "Previous")
        button_prev.connect("clicked", self.on_prev_clicked)
        button_prev.set_size_request(80, 40)
        button_close = Gtk.Button(label = "Close")
        button_close.connect("clicked", self.on_close_clicked)
        button_close.set_size_request(80, 40)
        button_next = Gtk.Button(label = "Next")
        button_next.connect("clicked", self.on_next_clicked)
        button_next.set_size_request(80, 40)

        box_main.pack_start(image, True, True, 0)
        box_main.pack_start(label, True, True, 0)
        box_main.pack_start(box_buttons, False, False, 0)
        box_buttons.pack_start(button_prev, True, True, 0)
        box_buttons.pack_start(button_close, True, True, 0)
        box_buttons.pack_start(button_next, True, True, 0)
        self.add(box_main)

    def on_prev_clicked(self, widget):
        self.destroy()
        v_through_z_window_x = V_Through_Z_Window_X()
        v_through_z_window_x.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        v_through_z_window_z = V_Through_Z_Window_Z()
        v_through_z_window_z.show_all()

###########################################################################

class V_Through_Z_Window_Z(Gtk.Window):
    def __init__(self):
        super().__init__(title="V Through Z")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/Z.png")
        label = Gtk.Label(label="")
        label.set_line_wrap(True)
        label.set_line_wrap_mode(Gtk.WrapMode.WORD)
        button_prev = Gtk.Button(label = "Previous")
        button_prev.connect("clicked", self.on_prev_clicked)
        button_prev.set_size_request(80, 40)
        button_close = Gtk.Button(label = "Close")
        button_close.connect("clicked", self.on_close_clicked)
        button_close.set_size_request(80, 40)
        button_next = Gtk.Button(label = "Repeat")
        button_next.connect("clicked", self.on_next_clicked)
        button_next.set_size_request(80, 40)

        box_main.pack_start(image, True, True, 0)
        box_main.pack_start(label, True, True, 0)
        box_main.pack_start(box_buttons, False, False, 0)
        box_buttons.pack_start(button_prev, True, True, 0)
        box_buttons.pack_start(button_close, True, True, 0)
        box_buttons.pack_start(button_next, True, True, 0)
        self.add(box_main)

    def on_prev_clicked(self, widget):
        self.destroy()
        v_through_z_window_y = V_Through_Z_Window_Y()
        v_through_z_window_y.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        v_through_z_window_v = V_Through_Z_Window_V()
        v_through_z_window_v.show_all()