from tkinter import *


def calculate_button():
    text_2["text"] = float(miles.get()) * 1.609


window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=200,height=100)
window.config(padx=50, pady=20)

miles = Entry(width=10)
miles.grid(row=0, column=0)

kilometers = 0

text_1 = Label(text=f"miles is equal to")
text_1.grid(row=0, column=1)

text_2 = Label(text=f"0")
text_2.grid(row=0, column=2)
text_2.config(pady=20)

text_3 = Label(text=f"kilometers")
text_3.grid(row=0, column=3)

button = Button(text="Calculate", command=calculate_button)
button.grid(row=1, column=1)
button.config(pady=20)

mainloop()
