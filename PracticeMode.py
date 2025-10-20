import gi
import random

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def choose_character(min_val=1, max_val=26):
    random_number = random.randint(min_val, max_val)
    return random_number

def open_window():
    character = choose_character()
    if character == 1:
        open_window_a = A()
        open_window_a.show_all()
    elif character == 2:
        open_window_a = B()
        open_window_a.show_all()
    elif character == 3:
        open_window_a = C()
        open_window_a.show_all()
    elif character == 4:
        open_window_a = D()
        open_window_a.show_all()
    elif character == 5:
        open_window_a = E()
        open_window_a.show_all()
    elif character == 6:
        open_window_a = F()
        open_window_a.show_all()
    elif character == 7:
        open_window_a = G()
        open_window_a.show_all()
    elif character == 8:
        open_window_a = H()
        open_window_a.show_all()
    elif character == 9:
        open_window_a = I()
        open_window_a.show_all()
    elif character == 10:
        open_window_a = J()
        open_window_a.show_all()
    elif character == 11:
        open_window_a = K()
        open_window_a.show_all()
    elif character == 12:
        open_window_a = L()
        open_window_a.show_all()
    elif character == 13:
        open_window_a = M()
        open_window_a.show_all()
    elif character == 14:
        open_window_a = N()
        open_window_a.show_all()
    elif character == 15:
        open_window_a = O()
        open_window_a.show_all()
    elif character == 16:
        open_window_a = P()
        open_window_a.show_all()
    elif character == 17:
        open_window_a = Q()
        open_window_a.show_all()
    elif character == 18:
        open_window_a = R()
        open_window_a.show_all()
    elif character == 19:
        open_window_a = S()
        open_window_a.show_all()
    elif character == 20:
        open_window_a = T()
        open_window_a.show_all()
    elif character == 21:
        open_window_a = U()
        open_window_a.show_all()
    elif character == 22:
        open_window_a = V()
        open_window_a.show_all()
    elif character == 23:
        open_window_a = W()
        open_window_a.show_all()
    elif character == 24:
        open_window_a = X()
        open_window_a.show_all()
    elif character == 25:
        open_window_a = Y()
        open_window_a.show_all()
    elif character == 26:
        open_window_a = Z()
        open_window_a.show_all()
    

class A(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/a.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "A":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was A")

####################################################

class B(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/b.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "B":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was B")

#####################################################

class C(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/c.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "C":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was C")

#######################################

class D(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/d.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "D":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was D")

#############################################

class E(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/e.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "E":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was E")

##########################################

class F(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/f.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "F":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was F")

###############################################

class G(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/g.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "G":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was G")

##################################################

class H(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/h.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "H":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was H")

##############################################

class I(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/i.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "I":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was I")

#########################################

class J(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/j.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "J":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was J")

################################################

class K(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/k.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "K":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was K")

#################################################

class L(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/l.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "L":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was L")

#################################################

class M(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/m.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "M":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was M")

#######################################################

class N(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/n.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "N":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was N")

########################################################

class O(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/o.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "O":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was O")

################################

class P(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/p.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "P":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was P")

#################################################

class Q(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/q.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "Q":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was Q")

#########################################################

class R(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/r.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "R":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was R")

#################################

class S(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/s.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "S":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was S")

################################################

class T(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/t.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "T":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was T")

###################################################

class U(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/u.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "U":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was U")

#######################################################

class V(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/v.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "V":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was V")

############################################

class W(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/w.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "W":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was W")

###############################################

class X(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/x.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "X":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was X")

####################################################

class Y(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/y.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "Y":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was Y")

#################################################

class Z(Gtk.Window):
    def __init__(self):
        super().__init__(title="Practice Mode")
        self.set_default_size(300, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("assets/z.png")
        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Type what you think this character is...")
        self.input.connect("activate", self.check_answer)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        check_button = Gtk.Button(label="Check answer")
        check_button.connect("clicked", self.check_answer)
        check_button.get_style_context().add_class("Button_Type_1")

        go_again = Gtk.Button(label="Go again")
        go_again.connect("clicked", self.go_again_hehe)
        go_again.get_style_context().add_class("Button_Type_1")

        type_the_answer = Gtk.Label(label="Type what letter you think this is.")

        self.answer = Gtk.Label(label="")

        button_box.add(check_button)
        button_box.add(go_again)

        box.add(image)
        box.add(type_the_answer)
        box.add(self.input)
        box.add(self.answer)
        box.add(button_box)

        self.add(box)

    def go_again_hehe(self, widget):
        self.destroy()
        open_window()

    def check_answer(self, widget):
        user_guess = self.input.get_text().strip().upper()
        if user_guess == "Z":
            self.answer.set_text("That's correct!")
        else:
            self.answer.set_text("Nope! The answer was Z")