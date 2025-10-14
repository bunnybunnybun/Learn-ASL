import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Grid Example")
        self.set_default_size(500,400)

        #------------------------------------------------------------

        main_box = Gtk.Box()
        main_box.set_border_width(10)
        self.notebook = Gtk.Notebook()
        self.notebook.set_tab_pos(Gtk.PositionType.TOP)

        #------------------------------------------------------------

        page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        page1.set_border_width(10)
        
        #------------------------------------------------------------

        numbers_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        numbers_page.set_border_width(10)

        letters_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        letters_page.set_border_width(10)


        nested_notebook = Gtk.Notebook()
        nested_notebook.set_tab_pos(Gtk.PositionType.TOP)
        nested_notebook.append_page(letters_page, Gtk.Label(label="Letters"))
        nested_notebook.append_page(numbers_page, Gtk.Label(label="Numbers"))

        page1.add(nested_notebook)

        #------------------------------------------------------------


        page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        page2.set_border_width(10)

        #------------------------------------------------------------

        self.notebook.append_page(page1, Gtk.Label(label="Lessons"))
        self.notebook.append_page(page2, Gtk.Label(label="Overview"))

        main_box.pack_start(self.notebook, True, True, 0)

        self.add(main_box)

    


win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()