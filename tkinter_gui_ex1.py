import tkinter
from tkinter import Tk

window = Tk()

window.title("GUI Program")
window.minsize(width=500, height=400)

my_label = tkinter.Label(text="First Name", font=("Arial", 12, "bold"))
my_label.pack(side="left")


window.mainloop()
