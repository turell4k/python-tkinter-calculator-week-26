import tkinter as tk

# Create Window
window = tk.Tk()

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
entry_frame = tk.Frame(relief=tk.RAISED, borderwidth=1)
entry_frame.grid(row=0, column=0, columnspan=4)
calculation_entry = tk.Entry(master=entry_frame, width=25)
calculation_entry.grid(row=0, column=0)

for c in range(4):

    for r in range(4):
        frame = tk.Frame(
            relief=tk.FLAT,
            borderwidth=3,
        )
        frame.grid(row=r+1, column=c)
        button = tk.Button(
            master=frame,
            text=button_texts[(r+1, c)]
        )
        button.pack()

# Run window
window.mainloop()
