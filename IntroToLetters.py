import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

########################################################################

class Intro_To_Letters_Window_1(Gtk.Window):
    def __init__(self):
        super().__init__(title="Intro to Letters")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        
        label = Gtk.Label(label="Generally, you want your palm facing out, towards whoever you are signaling to, when you are fingerspelling letters. Keep this in mind while practicing. Use your main hand to signal letters, and keep it a little to the side, instead of directly in front of you.")
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

        box_main.pack_start(label, True, True, 0)
        box_main.pack_start(box_buttons, False, False, 0)
        box_buttons.pack_start(button_prev, True, True, 0)
        box_buttons.pack_start(button_close, True, True, 0)
        box_buttons.pack_start(button_next, True, True, 0)
        self.add(box_main)

    def on_next_clicked(self, widget):
        self.destroy()
        intro_to_letters_window_2 = Intro_To_Letters_Window_2()
        intro_to_letters_window_2.show_all()


    def on_close_clicked(self, widget):
        self.destroy()

###########################################################################

class Intro_To_Letters_Window_2(Gtk.Window):
    def __init__(self):
        super().__init__(title="Intro to Letters")
        self.set_default_size(300, 300)

        box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing= 6)
        box_main.set_border_width(10)
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing= 6)
        box_buttons.set_border_width(10)

        
        label = Gtk.Label(label="Now, click on the A Through F button to begin learning how to sign the letters A through F. It will show you how to do the letters one at a time, with a photo and short bit of text describing how to make the right shape with your hand. Practice the shape, then go to the next letter. Once you reach the end, repeat it a few times. Then go to the next section. Remember that you can always come back if you forget something.")
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

        box_main.pack_start(label, True, True, 0)
        box_main.pack_start(box_buttons, False, False, 0)
        box_buttons.pack_start(button_prev, True, True, 0)
        box_buttons.pack_start(button_close, True, True, 0)
        box_buttons.pack_start(button_next, True, True, 0)
        self.add(box_main)

    def on_prev_clicked(self, widget):
        self.destroy()
        intro_to_letters_window_1 = Intro_To_Letters_Window_1()
        intro_to_letters_window_1.show_all()

    def on_next_clicked(self, widget):
        self.destroy()

    def on_close_clicked(self, widget):
        self.destroy()