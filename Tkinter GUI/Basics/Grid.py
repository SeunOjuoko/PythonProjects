import tkinter
from tkinter import Entry

window = tkinter.Tk()
window.title('Graphical User Interface (GUI)')
#Size of window
window.minsize(500, 300)
window.config(padx = 20, pady = 20)

#Label
label = tkinter.Label(text='This is a Label', font=("Arial", 24, "bold"))
label.config(text = "New Text")
label.grid(column = 0, row = 0)
label.config(padx = 50, pady = 50)

def button_clicked():
    print("Button clicked")
    New_Text = input.get()
    label.config(text = New_Text)

button = tkinter.Button(text = "Click Me", command = button_clicked)
label.grid(column = 1, row = 1)

input = Entry(width = 10)
text = input.get()
label.grid(column = 2, row = 2)

window.mainloop()