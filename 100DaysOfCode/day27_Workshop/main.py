from tkinter import *


def button_clicked():
    print("I was clicked.")
    my_label["text"] = input.get()


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label.", font=("arial", 24, "bold"))
#my_label.pack()
#my_label.place(x=160, y=120)
my_label.grid(column=0, row=0)


# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
#button.pack()

# Entry
input = Entry(width=10)
input.grid(column=4, row=2)
#input.pack()

new_button = Button(text="I'm New!")
new_button.grid(column=2, row=0)


window.mainloop()
