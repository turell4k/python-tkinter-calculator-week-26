import tkinter as tk

# Create Window
window = tk.Tk()
window.title("Calculator")

# Define event functions
def on_click_button(event):
    calculator.process_button_press(button=event.widget["text"])
    equation_field["text"] = calculator.display

def on_resized_window(event):
    equation_field["width"] = int(window.winfo_width()/9)


class Calculator():

    # Main functionary class

    def __init__(self):

        # Equation processed f.x. "2+2", eval() will process
        self.equation = ""

        # Main display
        self._display = ""
        # Base 2, 10 and 16 displays
        self.display_b10 = ""
        self.display_b2 = ""
        self.display_b16 = ""

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

        # Valid bases that can be converted to
        self.valid_bases = {
            "Base 10": 10,
            "Base 2": 2,
            "Base 16": 16
        }

    @property
    def display(self):
        try:
            # Check if equation is convertable
            int(self.equation)
        except ValueError:
            return self.equation
        else:
            return self._convert_to_base(
                number=self.equation,
                base_to=self.base
            )

    def _convert_to_base(self, number, base_to):
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
            b10_to_b16 = {
                0: "0", 1: "1", 2: "2", 3: "3",
                4: "4", 5: "5", 6: "6", 7: "7",
                8: "8", 9: "9", 10: "A", 11: "B",
                12: "C", 13: "D", 14: "E", 15: "F"}
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
                    result_hex += b10_to_b16[hex_digit_value]
            return result_hex
        else:
            print("Invalid input for _convert()")

    def process_button_press(self, button):

        print(self.base, self.equation)

        if button in self.valid_bases.keys():
                self.base = self.valid_bases[button]

        # Clear equation
        elif button == "C":
            self.equation = ""

        # Calculate equation
        elif button == "=":
            self.equation = eval(self.equation)

        elif button in self.valid_digits:
            try:
                eval(self.equation + button)
            except SyntaxError:
                pass
            else:
                if self.operator is None:
                    self.equation += button
                else:
                    self.equation += self.operator
                    self.equation += button
                    self.operator = None

        elif button in self.valid_operators:
            self.operator = button


# Initialize widgets
button_texts = {
    (1, 0): "7",
    (1, 1): "8",
    (1, 2): "9",
    (1, 3): "*",
    (1, 4): "Base 10",
    (2, 0): "4",
    (2, 1): "5",
    (2, 2): "6",
    (2, 3): "/",
    (2, 4): "Base 2",
    (3, 0): "1",
    (3, 1): "2",
    (3, 2): "3",
    (3, 3): "+",
    (3, 4): "Base 16",
    (4, 0): "=",
    (4, 1): "0",
    (4, 2): ".",
    (4, 3): "-",
    (4, 4): "C"
}


num_columns = 5
num_rows = 4

calculator = Calculator()

field_frame = tk.Frame(relief=tk.SUNKEN, borderwidth=1)
field_frame.grid(row=0, column=0, columnspan=num_columns)
equation_field = tk.Label(
    master=field_frame,
    text=calculator.display,
    width=33,
    fg="black",
    bg="white"
)
equation_field.grid(row=0, column=0)

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
