from tkinter import *

def convert():
    miles = float(input.get())
    kilometer = round(miles * 1.609344)
    result.config(text=kilometer)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=30)
window.config(padx=20, pady=20)

input = Entry(width=7)
input.grid(column=1, row=0)

miles = Label(text="Miles")
is_equal = Label(text="is equal to")
result = Label(text="0")
km = Label(text="km")
miles.grid(column=2, row=0)
is_equal.grid(column=0, row=1)
result.grid(column=1, row=1)
km.grid(column=2, row=1)

calculator = Button(text="Calculate", command=convert)
calculator.grid(column=1, row=2)



















window.mainloop()