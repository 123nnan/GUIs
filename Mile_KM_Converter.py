from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=10, pady=10)

# Entry
value_entry = Entry(width=5)
def converter():
    data = value_entry.get()
    km = int(data) * 1.60934
    converted_label.config(text=f'{round(km, 2)}')

# Labels
mile_label = Label(text="Miles")
is_equal_label = Label(text="is equal to")
converted_label = Label(text="0")
km_label = Label(text="Km")


# Button
calculate = Button(text="Convert", command=converter)

# Grids
value_entry.grid(column=1, row=0)
mile_label.grid(column=2, row=0)
is_equal_label.grid(column=0, row=1)
converted_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)
calculate.grid(column=2, row=2)
window.mainloop()
