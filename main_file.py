import tkinter as tk

# Create Window
window = tk.Tk()
window.title("Calculator")

# Define functions
def on_click_button(event):
    calculation_field["text"] = calculator.process_input(input=event.widget["text"])

def on_resized_window(event):
    calculation_field["width"] = int(window.winfo_width()/9)

# Main functioning class
class Calculator():

    def __init__(self):

        self.state = "digit1"
        self.display = ""
        self.valid_states = (
            "digit1",
            "operator1",
            "digit req",
            "digit2",
            "digit3+"
            "calculate"
        )
        self.valid_operators = (
            "+",
            "-",
            "*",
            "/"
        )

    def process_input(self, input):

        if input == "C":
            self.state = "digit1"
            self.display = ""
            return self.display
        elif self.state == "digit1" and input.isdigit():
            self.state = "operator1"
            self.display = "".join((self.display, input))
            return self.display
        elif self.state == "operator1" and input.isdigit():
            self.display = "".join((self.display, input))
            return self.display
        elif self.state == "operator1" and input in self.valid_operators:
            self.state = "digit2"
            self.display = "".join((self.display, input))
            return self.display
        elif self.state == "digit2" and input.isdigit():
            self.state = "calculate"
            self.display = "".join((self.display, input))
            return self.display
        elif self.state == "calculate" and input.isdigit():
            self.display = "".join((self.display, input))
            return self.display
        elif self.state == "calculate" and input in self.valid_operators:
            self.state = "digit3+"
            self.display = "".join((self.display, input))
            return self.display
        elif self.state == "digit3+" and input.isdigit():
            self.state = "calculate"
            self.display = "".join((self.display, input))
            return self.display
        elif self.state == "calculate" and input == "=":
            return eval(self.display)


# Initialize widgets
button_texts = {
    (1, 0): "7",
    (1, 1): "8",
    (1, 2): "9",
    (1, 3): "*",
    (1, 4): "(",
    (2, 0): "4",
    (2, 1): "5",
    (2, 2): "6",
    (2, 3): "/",
    (2, 4): ")",
    (3, 0): "1",
    (3, 1): "2",
    (3, 2): "3",
    (3, 3): "+",
    (3, 4): "",
    (4, 0): "C",
    (4, 1): "0",
    (4, 2): ".",
    (4, 3): "-",
    (4, 4): "="

}

num_columns = 5
num_rows = 4

calculator = Calculator()

field_frame = tk.Frame(relief=tk.SUNKEN, borderwidth=1)
field_frame.grid(row=0, column=0, columnspan=num_columns)
calculation_field = tk.Label(
    master=field_frame,
    text=calculator.display,
    width=33,
    fg="black",
    bg="white"
)
calculation_field.grid(row=0, column=0)

for c in range(num_columns):
    window.columnconfigure(c, weight=1, minsize=56)
    window.rowconfigure(c, weight=1, minsize=50)

    for r in range(num_rows):
        frame = tk.Frame(
            relief=tk.FLAT,
            borderwidth=3,
        )
        frame.grid(
            row=r+1,
            column=c,
            padx=5,
            pady=5
        )
        button = tk.Button(
            master=frame,
            text=button_texts[(r+1, c)],
            width=5,
            height=3,
            fg="black",
            bg="white"
        )
        button.bind("<Button-1>", on_click_button)
        button.pack()

window.bind("<Configure>", on_resized_window)

# Run window
window.mainloop()
