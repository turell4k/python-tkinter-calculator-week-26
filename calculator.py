"""
A simple calculator built with python and the tkinter module
It supports base 10, 2 and 16, and I have built the converter myself
"""

import tkinter as tk

# Create Window
window = tk.Tk()
window.title("Calculator")


# Define event functions
def on_click_button(event):
    # Tell calculator which button was pressed
    calculator.process_button_press(button=event.widget["text"])
    equation_label["text"] = calculator.display_equation
    base_label["text"] = calculator.display_base


def on_resized_window(event):
    # Resize equation label to match window size
    equation_label["width"] = int(window.winfo_width()/9)


class Calculator():

    # Main functionary class

    def __init__(self):

        # Equation processed f.x. "2+2", eval() will process
        self.equation = []
        self.max_equation_len = 100

        # Default is base 10
        self.base = 10

        # Operator buffer
        self.operator = None

        # Valid digits that will be accepted
        self.valid_digits = (
            ".",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "0",
            "00"
        )

        # Valid operators that will be accepted
        self.valid_operators = (
            "+",
            "-",
            "*",
            "/"
        )

        # Bases that are supported
        self.valid_bases = {
            "Base 10": 10,
            "Base 2": 2,
            "Base 16": 16
        }

        # Dictionary for converting base 10 numbers to base 16 digits
        self.b10_to_b16 = {
            0: "0", 1: "1", 2: "2", 3: "3",
            4: "4", 5: "5", 6: "6", 7: "7",
            8: "8", 9: "9", 10: "A", 11: "B",
            12: "C", 13: "D", 14: "E", 15: "F"
        }

    @property
    def display_equation(self):
        # Displays equation in current base

        if self.equation is []:
            return ""
        else:
            result = ""

            for e in self.equation:
                if e in self.valid_operators:
                    result += e
                else:
                    result += self._convert_to_base(
                        number=e,
                        base_to=self.base
                    )

            return result

    @property
    def display_base(self):
        # Displays current base
        return "Base " + str(self.base)

    def _convert_to_base(self, number, base_to):
        # Convert base 10 equation to hex/bin

        number = str(number)
        result = ""
        number_int = int(number)
        if base_to == 10:
            # Standard is base 10
            return number
        elif base_to == 2:
            # Number of digits necessary
            number_of_digits = 4
            while 2 ** number_of_digits <= number_int:
                number_of_digits += 4
            value = 0
            for n in reversed(range(0, number_of_digits)):
                if 2**n <= number_int-value:
                    value += 2**n
                    result += "1"
                else:
                    result += "0"
            return result

        # Convert to hex
        elif base_to == 16:
            number_of_hex_digits = 32
            result_hex = ""
            while 16 ** number_of_hex_digits <= number_int:
                number_of_hex_digits += 32
            for n in reversed(range(0, number_of_hex_digits)):
                pos_value = 16**n
                # Do we need this value?
                if pos_value <= number_int:
                    # 0-15 in this position
                    hex_digit_value = number_int // pos_value
                    # Subtract numeric value
                    number_int -= pos_value * hex_digit_value
                    # Add the hex digit to result
                    result_hex += self.b10_to_b16[hex_digit_value]
            return result_hex
        else:
            print("Error: Invalid input for _convert()")

    def process_button_press(self, button):
        # React on button press event

        # Make sure eval() and _convert_to_base() can handle equation
        if len("".join(self.equation)) > self.max_equation_len:
            self.equation = []
            print("Error: Equation too long")

        # Change base
        elif button in self.valid_bases.keys():
            self.base = self.valid_bases[button]

        # Clear equation
        elif button == "C":
            self.equation = []

        # Calculate equation
        elif button == "=":
            self.equation = [str(eval("".join(self.equation)))]

        # Only insert digit if operator buffer is empty. If not, add operator
        elif button in self.valid_digits:
            try:
                float(self.equation[-1] + button)
            except IndexError:
                self.equation.append(button)
            else:
                if self.operator is None and self.equation is not []:
                    self.equation[-1] += button
                elif self.operator is not None and self.equation is not []:
                    self.equation.append(self.operator)
                    self.equation.append(button)
                    self.operator = None
                else:
                    self.equation.append(button)

        # Add operator to buffer
        elif button in self.valid_operators:
            self.operator = button


# Initialize widgets

# Texts according to button position in grid
button_texts = {
    (1, 0): "7", (1, 1): "8",
    (1, 2): "9",(1, 3): "*",
    (1, 4): "Base 10", (2, 0): "4",
    (2, 1): "5", (2, 2): "6",
    (2, 3): "/", (2, 4): "Base 2",
    (3, 0): "1", (3, 1): "2",
    (3, 2): "3", (3, 3): "+",
    (3, 4): "Base 16", (4, 0): "=",
    (4, 1): "0", (4, 2): ".",
    (4, 3): "-", (4, 4): "C"
}


# Amount of rows and columns of widgets
num_columns = 5
num_rows = 4

# Initialize calculator
calculator = Calculator()

# Frames for equation label and base label
equation_frame = tk.Frame(relief=tk.SUNKEN, borderwidth=2)
equation_frame.grid(row=0, column=0, columnspan=num_columns-1)
base_frame = tk.Frame(relief=tk.RAISED, borderwidth=2)
base_frame.grid(row=0, column=num_columns-1)

# Initialize equation and base labels and position them in grid
equation_label = tk.Label(
    master=equation_frame,
    text="",
    width=1,
    fg="black",
    bg="white"
)
equation_label.grid(row=0, column=0)

base_label = tk.Label(
    master=base_frame,
    text=calculator.display_base,
    width=6,
    fg="black",
    bg="white"
)
base_label.grid(row=0, column=0)

# Create columns in grid
for c in range(num_columns):
    # Make window resizable
    window.columnconfigure(c, weight=1, minsize=56)
    window.rowconfigure(c, weight=1, minsize=50)

    # Create rows in grid
    for r in range(num_rows):
        # Create and position button frame
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
        # Create button and bind click function
        button = tk.Button(
            master=frame,
            text=button_texts[(r+1, c)],
            width=6,
            height=3,
            fg="black",
            bg="white"
        )
        button.bind("<Button-1>", on_click_button)
        button.pack()

# Bind resizing function to resizing event
window.bind("<Configure>", on_resized_window)

# Run window
window.mainloop()