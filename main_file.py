import tkinter as tk

# Create Window
window = tk.Tk()

# Define functions
def on_click_button(event):
    calculation_field["text"] = calculator.process_input(input=event.widget["text"])

class Calculator():

    def __init__(self, state="i1", display=""):

        self.state = state
        self.display = display
        self.valid_states = (
            "i1",
            "o1",
            "i2",
            "cc"
        )
        self.valid_operators = (
            "+",
            "-",
            "*",
            "/"
        )

    def process_input(self, input):

        if input == "C":
            self.display = ""
            return self.display
        elif self.state == "i1" and input.isdigit():
            self.state = "o1"
            self.display = "".join((self.display, input))
            return self.display
        elif self.state == "o1" and input.isdigit():
            self.display = "".join((self.display, input))
            return self.display
        elif self.state == "o1" and input in self.valid_operators:
            self.state = "i2"
            self.display = "".join((self.display, input))
            return self.display
        elif self.state == "i2" and input.isdigit():
            self.state = "cc"
            self.display = "".join((self.display, input))
            return self.display
        elif self.state == "cc" and input.isdigit():
            self.display = "".join((self.display, input))
            return self.display
        elif self.state == "cc" and input == "=":
            return eval(self.display)


# Initialize widgets
button_texts = {
    (1, 0): "7",
    (1, 1): "8",
    (1, 2): "9",
    (1, 3): "*",
    (2, 0): "4",
    (2, 1): "5",
    (2, 2): "6",
    (2, 3): "/",
    (3, 0): "1",
    (3, 1): "2",
    (3, 2): "3",
    (3, 3): "+",
    (4, 0): "C",
    (4, 1): "0",
    (4, 2): "=",
    (4, 3): "-"

}

calculator = Calculator()

field_frame = tk.Frame(relief=tk.SUNKEN, borderwidth=1)
field_frame.grid(row=0, column=0, columnspan=4)
calculation_field = tk.Label(master=field_frame, text=calculator.display, width=25)
calculation_field.grid(row=0, column=0)

for c in range(4):

    for r in range(4):
        frame = tk.Frame(
            relief=tk.FLAT,
            borderwidth=3,
        )
        frame.grid(row=r+1, column=c)
        button = tk.Button(
            master=frame,
            text=button_texts[(r+1, c)],
        )
        button.bind("<Button-1>", on_click_button)
        button.pack()

# Run window
window.mainloop()
