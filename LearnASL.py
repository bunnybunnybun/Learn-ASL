import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Grid Example")
        self.set_default_size(400,300)

        main_box = Gtk.Box()

        self.notebook = Gtk.Notebook()
        self.notebook.set_tab_pos(Gtk.PositionType.TOP)

        page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        page1.set_border_width(10)
        page1_label = Gtk.Label(label="Lesson tab content")
        page1.add(page1_label)

        page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        page2.set_border_width(10)
        page2_label = Gtk.Label(label="Overview tab content")
        page2_button = Gtk.Button(label="Temporary button")
        page2.add(page2_label)
        page2.add(page2_button)

        self.notebook.append_page(page1, Gtk.Label(label="Lessons"))
        self.notebook.append_page(page2, Gtk.Label(label="Overview"))

        main_box.pack_start(self.notebook, True, True, 0)

        self.add(main_box)


win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()