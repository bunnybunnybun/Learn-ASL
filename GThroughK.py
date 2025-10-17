import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

########################################################################

class G_Through_K_Window_G(Gtk.Window):
    def __init__(self):
        super().__init__(title="G Through K")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/G.png")
        label = Gtk.Label(label="Literaly just like you are pointing. You can also think of it as a finger gun but only with your index finger.")
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
        g_through_k_window_h = G_Through_K_Window_H()
        g_through_k_window_h.show_all()


    def on_close_clicked(self, widget):
        self.destroy()

###############################################################################

class G_Through_K_Window_H(Gtk.Window):
    def __init__(self):
        super().__init__(title="G Through K")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/H.png")
        label = Gtk.Label(label="Just like G, but with both your index and middle fingers.")
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
        g_through_k_window_g = G_Through_K_Window_G()
        g_through_k_window_g.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        g_through_k_window_i = G_Through_K_Window_I()
        g_through_k_window_i.show_all()

###########################################################################

class G_Through_K_Window_I(Gtk.Window):
    def __init__(self):
        super().__init__(title="G Through K")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/I.png")
        label = Gtk.Label(label="Point your pinky finger straight up, and fold your index, middle and ring fingers down. Fold your thumb in over your index and middle fingers.")
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
        g_through_k_window_h = G_Through_K_Window_H()
        g_through_k_window_h.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        g_through_k_window_j = G_Through_K_Window_J()
        g_through_k_window_j.show_all()

#####################################################################

class G_Through_K_Window_J(Gtk.Window):
    def __init__(self):
        super().__init__(title="G Through K")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/J.png")
        label = Gtk.Label(label="Just like an I, but swing your hand down and to the right (from your perspective), so that from the perspective of the person you are signaling to, it looks like the motion you made is in the shape of a J.")
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
        g_through_k_window_i = G_Through_K_Window_I()
        g_through_k_window_i.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        g_through_k_window_k = G_Through_K_Window_K()
        g_through_k_window_k.show_all()

###########################################################################

class G_Through_K_Window_K(Gtk.Window):
    def __init__(self):
        super().__init__(title="G Through K")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/K.png")
        label = Gtk.Label(label="Point your index and middle fingers straight up, sperated from each other. Fold your ring and pinky fingers down over your palm, and hold your thumb in front of the bottom of your index and middle fingers.")
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
        g_through_k_window_j = G_Through_K_Window_J()
        g_through_k_window_j.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        g_through_k_window_g = G_Through_K_Window_G()
        g_through_k_window_g.show_all()