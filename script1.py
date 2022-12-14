from tkinter import *
from tkinter import ttk

root = Tk()


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root.title("Feet To Meters")
main_frame = ttk.Frame(root, padding="3 3 12 12")
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(main_frame, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(main_frame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(main_frame, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(main_frame, text="Feet").grid(column=3, row=1, sticky=W)
ttk.Label(main_frame, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(main_frame, text="Meters").grid(column=3, row=2, sticky=W)

for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()