import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

########################################################################

class L_Through_P_Window_L(Gtk.Window):
    def __init__(self):
        super().__init__(title="L Through P")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/L.png")
        label = Gtk.Label(label="Create an L shape with your index finger and thumb. Fold your other three fingers down over your palm.")
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
        l_through_p_window_m = L_Through_P_Window_M()
        l_through_p_window_m.show_all()


    def on_close_clicked(self, widget):
        self.destroy()

###############################################################################

class L_Through_P_Window_M(Gtk.Window):
    def __init__(self):
        super().__init__(title="L Through P")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/M.png")
        label = Gtk.Label(label="Fold your pinky finger down, and stick your thumb in between your pinky and ring finers. Fold your index, middle and ring fingers down over your thumb.")
        label.set_line_wrap(True)
        label.set_line_wrap_mode(Gtk.WrapMode.WORD)
        button_prev = Gtk.Button(label = "Previous")
        button_prev.connect("clicked", self.on_prev_clicked)
        button_prev.get_style_context().add_class("Button_Type_2")
        button_prev.set_size_request(80, 40)
        button_close = Gtk.Button(label = "Close")
        button_close.connect("clicked", self.on_close_clicked)
        button_close.get_style_context().add_class("Button_Type_2")
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
        l_through_p_window_l = L_Through_P_Window_L()
        l_through_p_window_l.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        l_through_p_window_n = L_Through_P_Window_N()
        l_through_p_window_n.show_all()

###########################################################################

class L_Through_P_Window_N(Gtk.Window):
    def __init__(self):
        super().__init__(title="L Through P")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/N.png")
        label = Gtk.Label(label="Fold your ring and pinky fingers down, stick your thumb in between your middle finger and ring finger, then fold your index and middle fingers over your thumb.")
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
        l_through_p_window_m = L_Through_P_Window_M()
        l_through_p_window_m.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        l_through_p_window_o = L_Through_P_Window_O()
        l_through_p_window_o.show_all()

#####################################################################

class L_Through_P_Window_O(Gtk.Window):
    def __init__(self):
        super().__init__(title="L Through P")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/O.png")
        label = Gtk.Label(label="Form an O shape using your index, middle, ring and pinky fingers as the top part of the O, and your thumb as the bottom part.")
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
        l_through_p_window_n = L_Through_P_Window_N()
        l_through_p_window_n.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        l_through_p_window_p = L_Through_P_Window_P()
        l_through_p_window_p.show_all()

###########################################################################

class L_Through_P_Window_P(Gtk.Window):
    def __init__(self):
        super().__init__(title="L Through P")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/P.png")
        label = Gtk.Label(label="Point your index finger out, and down a little. Touch your thumb to the tip of your middle finger, and fold in your ring and pinky fingers.")
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
        l_through_p_window_o = L_Through_P_Window_O()
        l_through_p_window_o.show_all()

    def on_close_clicked(self, widget):
        self.destroy()

    def on_next_clicked(self, widget):
        self.destroy()
        l_through_p_window_l = L_Through_P_Window_L()
        l_through_p_window_l.show_all()