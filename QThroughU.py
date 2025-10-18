import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

########################################################################

class Q_Through_U_Window_Q(Gtk.Window):
    def __init__(self):
        super().__init__(title="Q Through U")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/Q.png")
        label = Gtk.Label(label="Curl your middle, ring, and pinky fingers in as if you are making a fist. Then, point your thumb and index fingers straight down.")
        label.set_line_wrap(True)
        label.set_line_wrap_mode(Gtk.WrapMode.WORD)
        button_prev = Gtk.Button(label = "Previous")
        button_prev.get_style_context().add_class("Button_Type_2")
        button_prev.set_size_request(80, 40)
        button_close = Gtk.Button(label = "Close")
        button_close.get_style_context().add_class("Button_Type_2")
        button_close.connect("clicked", self.on_close_clicked)
        button_close.set_size_request(80, 40)
        button_next = Gtk.Button(label = "Next")
        button_next.get_style_context().add_class("Button_Type_2")
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
        q_through_u_window_r = Q_Through_U_Window_R()
        q_through_u_window_r.show_all()


    def on_close_clicked(self, widget):
        self.destroy()

###############################################################################

class Q_Through_U_Window_R(Gtk.Window):
    def __init__(self):
        super().__init__(title="Q Through U")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/R.png")
        label = Gtk.Label(label="Point your middle finger up, with your index finger crossed in front of it. Fold your ring and pinky fingers down, and put your thumb in front of your ring finger.")
        label.set_line_wrap(True)
        label.set_line_wrap_mode(Gtk.WrapMode.WORD)
        button_prev = Gtk.Button(label = "Previous")
        button_prev.get_style_context().add_class("Button_Type_2")
        button_prev.connect("clicked", self.on_prev_clicked)
        button_prev.set_size_request(80, 40)
        button_close = Gtk.Button(label = "Close")
        button_close.get_style_context().add_class("Button_Type_2")
        button_close.connect("clicked", self.on_close_clicked)
        button_close.set_size_request(80, 40)
        button_next = Gtk.Button(label = "Next")
        button_next.get_style_context().add_class("Button_Type_2")
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
        q_through_u_window_q = Q_Through_U_Window_Q()
        q_through_u_window_q.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        q_through_u_window_s = Q_Through_U_Window_S()
        q_through_u_window_s.show_all()

###########################################################################

class Q_Through_U_Window_S(Gtk.Window):
    def __init__(self):
        super().__init__(title="Q Through U")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/S.png")
        label = Gtk.Label(label="Create a fist, then fold your thumb in front of your index and middle fingers.")
        label.set_line_wrap(True)
        label.set_line_wrap_mode(Gtk.WrapMode.WORD)
        button_prev = Gtk.Button(label = "Previous")
        button_prev.get_style_context().add_class("Button_Type_2")
        button_prev.connect("clicked", self.on_prev_clicked)
        button_prev.set_size_request(80, 40)
        button_close = Gtk.Button(label = "Close")
        button_close.get_style_context().add_class("Button_Type_2")
        button_close.connect("clicked", self.on_close_clicked)
        button_close.set_size_request(80, 40)
        button_next = Gtk.Button(label = "Next")
        button_next.get_style_context().add_class("Button_Type_2")
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
        q_through_u_window_r = Q_Through_U_Window_R()
        q_through_u_window_r.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        q_through_u_window_t = Q_Through_U_Window_T()
        q_through_u_window_t.show_all()

#####################################################################

class Q_Through_U_Window_T(Gtk.Window):
    def __init__(self):
        super().__init__(title="Q Through U")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/T.png")
        label = Gtk.Label(label="Create a fist, then stick your thumb right in between your index and middle fingers, with your index finger folding over the lower part of your thumb.")
        label.set_line_wrap(True)
        label.set_line_wrap_mode(Gtk.WrapMode.WORD)
        button_prev = Gtk.Button(label = "Previous")
        button_prev.get_style_context().add_class("Button_Type_2")
        button_prev.connect("clicked", self.on_prev_clicked)
        button_prev.set_size_request(80, 40)
        button_close = Gtk.Button(label = "Close")
        button_close.get_style_context().add_class("Button_Type_2")
        button_close.connect("clicked", self.on_close_clicked)
        button_close.set_size_request(80, 40)
        button_next = Gtk.Button(label = "Next")
        button_next.get_style_context().add_class("Button_Type_2")
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
        q_through_u_window_s = Q_Through_U_Window_S()
        q_through_u_window_s.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        q_through_u_window_u = Q_Through_U_Window_U()
        q_through_u_window_u.show_all()

###########################################################################

class Q_Through_U_Window_U(Gtk.Window):
    def __init__(self):
        super().__init__(title="Q Through U")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/U.png")
        label = Gtk.Label(label="Point your index and middle fingers straight up, touching each other. Fold down your ring and pinky fingers, and fold your thumb over your ring finger.")
        label.set_line_wrap(True)
        label.set_line_wrap_mode(Gtk.WrapMode.WORD)
        button_prev = Gtk.Button(label = "Previous")
        button_prev.get_style_context().add_class("Button_Type_2")
        button_prev.connect("clicked", self.on_prev_clicked)
        button_prev.set_size_request(80, 40)
        button_close = Gtk.Button(label = "Close")
        button_close.get_style_context().add_class("Button_Type_2")
        button_close.connect("clicked", self.on_close_clicked)
        button_close.set_size_request(80, 40)
        button_next = Gtk.Button(label = "Repeat")
        button_next.get_style_context().add_class("Button_Type_2")
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
        q_through_u_window_t = Q_Through_U_Window_T()
        q_through_u_window_t.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        q_through_u_window_q = Q_Through_U_Window_Q()
        q_through_u_window_q.show_all()