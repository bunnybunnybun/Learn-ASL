import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

########################################################################

class A_Through_F_Window_A(Gtk.Window):
    def __init__(self):
        super().__init__(title="A Through F")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/A.png")
        label = Gtk.Label(label="Form a fist, with your thumb off to the side.")
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
        a_through_f_window_b = A_Through_F_Window_B()
        a_through_f_window_b.show_all()


    def on_close_clicked(self, widget):
        self.destroy()

###############################################################################

class A_Through_F_Window_B(Gtk.Window):
    def __init__(self):
        super().__init__(title="A Through F")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/B.png")
        label = Gtk.Label(label="Point all your fingers except your thumb straight up, and fold your thumb in over your palm.")
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
        a_through_f_window_a = A_Through_F_Window_A()
        a_through_f_window_a.show_all()

    def on_close_clicked(self, widget):
        self.destroy()
        a_through_f_window_c = A_Through_F_Window_C()

    def on_next_clicked(self, widget):
        self.destroy()
        a_through_f_window_c = A_Through_F_Window_C()
        a_through_f_window_c.show_all()

###########################################################################

class A_Through_F_Window_C(Gtk.Window):
    def __init__(self):
        super().__init__(title="A Through F")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/C.png")
        label = Gtk.Label(label="Create the shape of a C with your hand. Use your thumb for the bottom of the C and the rest of your fingers for the top.")
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
        a_through_f_window_b = A_Through_F_Window_B()
        a_through_f_window_b.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        a_through_f_window_d = A_Through_F_Window_D()
        a_through_f_window_d.show_all()

#####################################################################

class A_Through_F_Window_D(Gtk.Window):
    def __init__(self):
        super().__init__(title="A Through F")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/D.png")
        label = Gtk.Label(label="Point your index finger straight up, and fold your middle, ring, and pinky fingers down and touch your thumb to the tip of your middle finger.")
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
        a_through_f_window_c = A_Through_F_Window_C()
        a_through_f_window_c.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        a_through_f_window_e = A_Through_F_Window_E()
        a_through_f_window_e.show_all()

###########################################################################

class A_Through_F_Window_E(Gtk.Window):
    def __init__(self):
        super().__init__(title="A Through F")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/E.png")
        label = Gtk.Label(label="Create a fist, with your thumb folded in over your other four fingers.")
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
        a_through_f_window_d = A_Through_F_Window_D()
        a_through_f_window_d.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        a_through_f_window_f = A_Through_F_Window_F()
        a_through_f_window_f.show_all()

###########################################################################

class A_Through_F_Window_F(Gtk.Window):
    def __init__(self):
        super().__init__(title="A Through F")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/F.png")
        label = Gtk.Label(label="Point your middle, ring and pinky fingers straight up, and put your thumb and index fingers together to create an O.")
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
        a_through_f_window_e = A_Through_F_Window_E()
        a_through_f_window_e.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        a_through_f_window_a = A_Through_F_Window_A()
        a_through_f_window_a.show_all()