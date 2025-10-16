import gi
import IntroToLetters
import AThroughF
import GThroughK

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="LearnASL")
        self.set_default_size(500,400)

        #------------------------------------------------------------

        main_box = Gtk.Box()
        main_box.set_border_width(10)
        self.notebook = Gtk.Notebook()
        self.notebook.set_tab_pos(Gtk.PositionType.TOP)

        #____________________________________________________________

        page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        page1.set_border_width(10)
        
        #____________________________________________________________

        numbers_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        numbers_page.set_border_width(10)

        letters_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        letters_page.set_border_width(10)
        #------------------------------------------------------------

        intro_to_letters = Gtk.Button(label="Intro to Letters")
        intro_to_letters.connect("clicked", self.open_intro_to_letters)
        intro_to_letters.set_border_width(8)
        letter_button1 = Gtk.Button(label="A Through F")
        letter_button1.connect("clicked", self.open_a_through_f)
        letter_button1.set_border_width(8)
        letter_button2 = Gtk.Button(label="G Through K")
        letter_button2.connect("clicked", self.open_g_through_k)
        letter_button2.set_border_width(8)
        letter_button3 = Gtk.Button(label="L Through P")
        letter_button3.set_border_width(8)
        letter_button4 = Gtk.Button(label="Q Through U")
        letter_button4.set_border_width(8)
        letter_button5 = Gtk.Button(label="V Through Z")
        letter_button5.set_border_width(8)

        letter_grid = Gtk.Grid()
        letter_grid.attach(intro_to_letters, 1, 0, 1, 1)
        letter_grid.attach_next_to(letter_button1, intro_to_letters, Gtk.PositionType.RIGHT, 1, 1)
        letter_grid.attach_next_to(letter_button2, letter_button1, Gtk.PositionType.RIGHT, 1, 1)
        letter_grid.attach_next_to(letter_button3, intro_to_letters, Gtk.PositionType.BOTTOM, 1, 1)
        letter_grid.attach_next_to(letter_button4, letter_button3, Gtk.PositionType.RIGHT, 1, 1)
        letter_grid.attach_next_to(letter_button5, letter_button4, Gtk.PositionType.RIGHT, 1, 1)
        letters_page.add(letter_grid)

        #------------------------------------------------------------

        number_intro_button = Gtk.Button(label="Intro to numbers")
        number_intro_button.set_border_width(8)
        number_button1 = Gtk.Button(label="0 Through 9")
        number_button1.set_border_width(8)
        number_button2 = Gtk.Button(label="10 Through 19")
        number_button2.set_border_width(8)
        number_button3 = Gtk.Button(label="20 Through 29")
        number_button3.set_border_width(8)
        number_button4 = Gtk.Button(label="30 Through 39")
        number_button4.set_border_width(8)
        number_button5 = Gtk.Button(label="40 Through 49")
        number_button5.set_border_width(8)
        number_button6 = Gtk.Button(label="50 Through 59")
        number_button6.set_border_width(8)
        number_button7 = Gtk.Button(label="60 Through 69")
        number_button7.set_border_width(8)
        number_button8 = Gtk.Button(label="70 Through 79")
        number_button8.set_border_width(8)
        number_button9 = Gtk.Button(label="80 Through 89")
        number_button9.set_border_width(8)
        number_button10 = Gtk.Button(label="90 Through 100")
        number_button10.set_border_width(8)

        number_grid = Gtk.Grid()
        number_grid.add(number_intro_button)
        number_grid.attach(number_button1, 1, 0, 1, 1)
        number_grid.attach_next_to(number_button2, number_button1, Gtk.PositionType.RIGHT, 1, 1)
        number_grid.attach_next_to(number_button3, number_intro_button, Gtk.PositionType.BOTTOM, 1, 1)
        number_grid.attach_next_to(number_button4, number_button3, Gtk.PositionType.RIGHT, 1, 1)
        number_grid.attach_next_to(number_button5, number_button4, Gtk.PositionType.RIGHT, 1, 1)
        number_grid.attach_next_to(number_button6, number_button3, Gtk.PositionType.BOTTOM, 1, 1)
        number_grid.attach_next_to(number_button7, number_button6, Gtk.PositionType.RIGHT, 1, 1)
        number_grid.attach_next_to(number_button8, number_button7, Gtk.PositionType.RIGHT, 1, 1)
        number_grid.attach_next_to(number_button9, number_button6, Gtk.PositionType.BOTTOM, 1, 1)
        number_grid.attach_next_to(number_button10, number_button9, Gtk.PositionType.RIGHT, 1, 1)

        numbers_page.add(number_grid)

        #------------------------------------------------------------

        nested_notebook = Gtk.Notebook()
        nested_notebook.set_tab_pos(Gtk.PositionType.TOP)
        nested_notebook.append_page(letters_page, Gtk.Label(label="Letters"))
        nested_notebook.append_page(numbers_page, Gtk.Label(label="Numbers"))

        page1.add(nested_notebook)

        #____________________________________________________________


        page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        page2.set_border_width(10)

        #____________________________________________________________

        self.notebook.append_page(page1, Gtk.Label(label="Lessons"))
        self.notebook.append_page(page2, Gtk.Label(label="Overview"))

        main_box.pack_start(self.notebook, True, True, 0)

        self.add(main_box)

    #__________________________________________________________________

    def open_intro_to_letters(self, widget):
        intro_to_letters_window_1 = IntroToLetters.Intro_To_Letters_Window_1()
        intro_to_letters_window_1.show_all()

    def open_a_through_f(self, widget):
        a_through_f_window = AThroughF.A_Through_F_Window_A()
        a_through_f_window.show_all()

    def open_g_through_k(self, widget):
        g_through_k_window = GThroughK.G_Through_K_Window_G()
        g_through_k_window.show_all()

    
    

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()