import gi
import IntroToLetters
import AThroughF
import GThroughK
import LThroughP
import QThroughU
import VThroughZ
import PracticeMode

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

css_provider = Gtk.CssProvider()

css = '''
stackswitcher {
    
}

button.Button_Type_1 {
    border-radius: 12px;
    min-width: 120px;
    min-height: 25px;
    box-shadow: 3px 5px 5px rgba(0, 0, 0, 0.5);
    margin: 2px;
    background: linear-gradient(180deg, rgba(10,119,127,1) 0%, rgba(6,74,79,1) 100%);
    color: white;
}

button.Button_Type_1:hover {
    background: rgba(13,158,168,1);
    font-size: 1.2em;
    min-height: 33px;
    min-width: 135px;
}

button.Button_Type_2 {
    border-radius: 12px;
    box-shadow: 3px 5px 5px rgba(0, 0, 0, 0.5);
    margin: 10px;
    background: linear-gradient(180deg, rgba(10,119,127,1) 0%, rgba(6,74,79,1) 100%);
    color: white;
}

button.Button_Type_2:hover {
    background: rgba(13,158,168,1);
    font-size: 1.2em;
    min-height: 30px;
    min-width: 90px;
}

button.close {
    color: red;
    min-width: 10px;
    min-height: 10px;
    border-radius: 50px;
    padding: 0px 10px;
    font-size: 20px;
}

box.nested_box {
    border: 3px solid rgba(37, 37, 37, 1);
}

box.switcher {
    background: linear-gradient(180deg, rgba(10,119,127,1) 85%, rgba(6,74,79,1) 100%);
}

box.page2 {
    border: 3px solid rgba(37, 37, 37, 1)
}

box.page3 {
    border: 3px solid rgba(37, 37, 37, 1)
}

label.disclaimer {
    color: red;
}
'''

css_provider.load_from_data(css.encode())

settings = Gtk.Settings.get_default()
settings.set_property("gtk-theme-name", "Adwaita")
settings.set_property("gtk-application-prefer-dark-theme", True)

screen = Gdk.Screen.get_default()
style_context = Gtk.StyleContext()
style_context.add_provider_for_screen(
    screen,
    css_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="LearnASL")
        self.set_default_size(588,437)
        self.set_decorated(False)

        #------------------------------------------------------------

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        main_box.set_border_width(0)
        
        #self.notebook = Gtk.Notebook()
        #self.notebook.set_tab_pos(Gtk.PositionType.TOP)

        

        #____________________________________________________________

        page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        page1.set_border_width(10)
        
        #____________________________________________________________

        numbers_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        numbers_page.set_border_width(2)

        letters_page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        letters_page.set_border_width(2)
        #------------------------------------------------------------

        intro_to_letters = Gtk.Button(label="Intro to Letters")
        intro_to_letters.connect("clicked", self.open_intro_to_letters)
        intro_to_letters.get_style_context().add_class("Button_Type_1")
        intro_to_letters.set_border_width(8)
        letter_button1 = Gtk.Button(label="A Through F")
        letter_button1.connect("clicked", self.open_a_through_f)
        letter_button1.get_style_context().add_class("Button_Type_1")
        letter_button1.set_border_width(8)
        letter_button2 = Gtk.Button(label="G Through K")
        letter_button2.connect("clicked", self.open_g_through_k)
        letter_button2.get_style_context().add_class("Button_Type_1")
        letter_button2.set_border_width(8)
        letter_button3 = Gtk.Button(label="L Through P")
        letter_button3.connect("clicked", self.open_l_through_p)
        letter_button3.get_style_context().add_class("Button_Type_1")
        letter_button3.set_border_width(8)
        letter_button4 = Gtk.Button(label="Q Through U")
        letter_button4.connect("clicked", self.open_q_through_u)
        letter_button4.get_style_context().add_class("Button_Type_1")
        letter_button4.set_border_width(8)
        letter_button5 = Gtk.Button(label="V Through Z")
        letter_button5.connect("clicked", self.open_v_through_z)
        letter_button5.get_style_context().add_class("Button_Type_1")
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
        number_intro_button.get_style_context().add_class("Button_Type_1")
        number_intro_button.set_border_width(8)
        number_button1 = Gtk.Button(label="0 Through 9")
        number_button1.get_style_context().add_class("Button_Type_1")
        number_button1.set_border_width(8)
        number_button2 = Gtk.Button(label="10 Through 19")
        number_button2.get_style_context().add_class("Button_Type_1")
        number_button2.set_border_width(8)
        number_button3 = Gtk.Button(label="20 Through 29")
        number_button3.get_style_context().add_class("Button_Type_1")
        number_button3.set_border_width(8)
        number_button4 = Gtk.Button(label="30 Through 39")
        number_button4.get_style_context().add_class("Button_Type_1")
        number_button4.set_border_width(8)
        number_button5 = Gtk.Button(label="40 Through 49")
        number_button5.get_style_context().add_class("Button_Type_1")
        number_button5.set_border_width(8)
        number_button6 = Gtk.Button(label="50 Through 59")
        number_button6.get_style_context().add_class("Button_Type_1")
        number_button6.set_border_width(8)
        number_button7 = Gtk.Button(label="60 Through 69")
        number_button7.get_style_context().add_class("Button_Type_1")
        number_button7.set_border_width(8)
        number_button8 = Gtk.Button(label="70 Through 79")
        number_button8.get_style_context().add_class("Button_Type_1")
        number_button8.set_border_width(8)
        number_button9 = Gtk.Button(label="80 Through 89")
        number_button9.get_style_context().add_class("Button_Type_1")
        number_button9.set_border_width(8)
        number_button10 = Gtk.Button(label="90 Through 100")
        number_button10.get_style_context().add_class("Button_Type_1")
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

        #nested_notebook = Gtk.Notebook()
        #nested_notebook.set_tab_pos(Gtk.PositionType.TOP)
        #nested_notebook.append_page(letters_page, Gtk.Label(label="Letters"))
        #nested_notebook.append_page(numbers_page, Gtk.Label(label="Numbers"))

        #page1.add(nested_notebook)

        #____________________________________________________________

        nested_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        nested_box.set_border_width(10)
        nested_box.get_style_context().add_class("nested_box")
        page1.add(nested_box)

        
        nested_stack = Gtk.Stack()
        nested_stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        nested_stack.set_transition_duration(500)
        nested_stack.add_titled(letters_page, "letters_page", "Letters")
        nested_stack.add_titled(numbers_page, "numbers_page", "Numbers")

        nested_switcher = Gtk.StackSwitcher()
        nested_switcher.set_stack(nested_stack)
        nested_switcher.set_border_width(10)

        nested_box.add(nested_switcher)
        nested_box.add(nested_stack)

        #--------------------------------------------------------------

        page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        page2.get_style_context().add_class("page2")
        page2.set_border_width(10)
        page_2_inner_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        page_2_inner_box.set_border_width(10)
        practice_button = Gtk.Button(label="Practice mode!")
        practice_button.connect("clicked", self.practice_mode)
        practice_button.get_style_context().add_class("Button_Type_1")
        page_2_inner_box.add(practice_button)
        page2.add(page_2_inner_box)

        #-------------------------------------------------------------------

        page3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        page3.set_border_width(10)
        page3.get_style_context().add_class("page3")

        page_3_inner_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        page_3_inner_box.set_border_width(20)

        about_label_1 = Gtk.Label(label="This is a WIP app for learning how to fingerspell in American Sign Language!")
        about_label_1.set_line_wrap(True)
        about_label_2 = Gtk.Label(label="Disclaimer! I, the person who wrote this program, am NOT an ASL expert! Information provided in this app may be innacurate, so take it how you will.")
        about_label_2.set_line_wrap(True)
        about_label_2.get_style_context().add_class("disclaimer")


        page_3_inner_box.add(about_label_1)
        page_3_inner_box.add(about_label_2)
        page3.add(page_3_inner_box)

        #-------------------------------------------------------------------

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(500)

        stack.add_titled(page1, "page1", "Lessons")
        stack.add_titled(page2, "page2", "Overview")
        stack.add_titled(page3, "page3", "About")

        switcher = Gtk.StackSwitcher()
        switcher.set_stack(stack)
        switcher.set_border_width(10)

        close_button = Gtk.Button(label="X")
        close_button.connect("clicked", self.close)
        close_button.set_border_width(10)
        close_button.get_style_context().add_class("close")

        switcher_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        switcher_box.add(switcher)
        switcher_box.pack_end(close_button, False, False, 0)
        switcher_box.get_style_context().add_class("switcher")

        main_box.pack_start(switcher_box, False, False, 0)
        main_box.pack_start(stack, True, True, 0)

        #____________________________________________________________

        #self.notebook.append_page(page1, Gtk.Label(label="Lessons"))
        #self.notebook.append_page(page2, Gtk.Label(label="Overview"))

        #main_box.pack_start(self.notebook, True, True, 0)

        self.add(main_box)

    #__________________________________________________________________

    def close(self, widget):
        win.destroy()

    def practice_mode(self, widget):
        PracticeMode.open_window()
        

    def open_intro_to_letters(self, widget):
        intro_to_letters_window_1 = IntroToLetters.Intro_To_Letters_Window_1()
        intro_to_letters_window_1.show_all()

    def open_a_through_f(self, widget):
        a_through_f_window = AThroughF.A_Through_F_Window_A()
        a_through_f_window.show_all()

    def open_g_through_k(self, widget):
        g_through_k_window = GThroughK.G_Through_K_Window_G()
        g_through_k_window.show_all()

    def open_l_through_p(self, widget):
        l_through_p_window = LThroughP.L_Through_P_Window_L()
        l_through_p_window.show_all()

    def open_q_through_u(self, widget):
        q_through_u_window = QThroughU.Q_Through_U_Window_Q()
        q_through_u_window.show_all()
    
    def open_v_through_z(self, widget):
        v_through_z_window = VThroughZ.V_Through_Z_Window_V()
        v_through_z_window.show_all()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()