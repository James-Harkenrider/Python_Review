from tkinter import *


def miles_to_km():
    km = int(miles.get()) * 1.6
    km_answer_label["text"] = km


window = Tk()
window.minsize(width=200, height=120)
window.config(padx=20, pady=20)

miles = Entry(width=10)
miles.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_answer_label = Label(text="0")
km_answer_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)


window.mainloop()
