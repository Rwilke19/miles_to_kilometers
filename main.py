from tkinter import *

window = Tk()
window.title("Miles to Kms Converter")
window.minsize(500, 300)
window.config(padx=20, pady=20)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

km = Label(text="Km")
km.grid(row=1, column=2)

equal = Label(text="is equal to")
equal.grid(row=1, column = 0)

label = Label(text=" ")
label.grid(row=1, column=1)

input = Entry(width=10)
input.grid(row=0, column=1)

def calculate():
    miles = float(input.get())
    calc = miles * 1.6
    str(calc)
    label.config(text=calc)

button = Button(text="Calculate", command=calculate)
button.grid(row=3, column=1)


window.mainloop()