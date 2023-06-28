import tkinter as tk

# Create Window
window = tk.Tk()
window.title("Calculator")

# Define event functions
def on_click_button(event):
    calculator.process_input(input=event.widget["text"])
    equation_field["text"] = calculator.display

def on_resized_window(event):
    equation_field["width"] = int(window.winfo_width()/9)


class Calculator():

    # Main functionary class

    def __init__(self):

        # Equation processed
        self.equation = ""

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

    @property
    def display(self):
        # Returns equation as str
        return self.equation

    def _calculate(self, result=""):

        # Calculate first part of equation
        if self.equation[1] == "+":
            result += str(float(self.equation[0]) + float(self.equation[2]))
        elif self.equation[1] == "-":
            result += str(float(self.equation[0]) - float(self.equation[2]))
        elif self.equation[1] == "*":
            result += str(float(self.equation[0]) * float(self.equation[2]))
        elif self.equation[1] == "/":
            result += str(float(self.equation[0]) / float(self.equation[2]))

        # Remove finished part of equation
        for n in range(2):
            self.equation.pop(1)
        self.equation[0] = result

        # If calculation is not finished, repeat
        if len(self.equation) > 1:
            self._calculate(result=result)

    def process_input(self, input):

        # Clear equation
        if input == "C":
            self.equation = ""

        # Calculate equation
        elif input == "=":
            self.equation = eval(self.equation)
            #self._calculate()

        elif input in self.valid_digits:
            try:
                eval(self.equation + input)
            except SyntaxError:
                pass
            else:
                if self.operator is None:
                    self.equation += input
                else:
                    self.equation += self.operator
                    self.equation += input
                    self.operator = None

        elif input in self.valid_operators:
            self.operator = input

        """
        # Insert digit
        elif input in self.valid_digits:
            # Check if equation is valid
            try:
                float(self.equation[-1] + input)
            except ValueError:
                if self.equation[-1] in self.valid_operators:
                    self.equation.append(input)
            else:
                self.equation[-1] = self.equation[-1] + input

        # Insert operator
        elif input in self.valid_operators:
            if self.equation[-1][-1].isdigit():
                self.equation.append(input)
            else:
                pass
        else:
            # Error if input is invalid
            raise ValueError("Invalid input:", input)
        """


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
    (3, 4): "=",
    (4, 0): "00",
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
