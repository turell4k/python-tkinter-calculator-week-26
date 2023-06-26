import tkinter as tk

# Create Window
window = tk.Tk()

# Initialize widgets

button_texts = {
    (0, 0): "7",
    (0, 1): "8",
    (0, 2): "9",
    (1, 0): "4",
    (1, 1): "5",
    (1, 2): "6",
    (2, 0): "1",
    (2, 1): "2",
    (2, 2): "3",
    (3, 0): ".",
    (3, 1): "0",
    (3, 2): " "

}

for c in range(3):
    for r in range(4):
        frame = tk.Frame(
            relief=tk.FLAT,
            borderwidth=3,
        )
        frame.grid(row=r, column=c)
        button = tk.Button(
            master=frame,
            text=button_texts[(r, c)]
        )
        button.pack()

# Run window
window.mainloop()
