import tkinter
from tkinter import Entry

window = tkinter.Tk()
window.title('Graphical User Interface (GUI)')
#Size of window
window.minsize(500, 300)

#Label
label = tkinter.Label(text='This is a Label', font=("Arial", 24, "bold"))
label.config(text = "New Text")
label.place(x = 100, y = 100)

def button_clicked():
    print("Button clicked")
    New_Text = input.get()
    label.config(text = New_Text)

button = tkinter.Button(text = "Click Me", command = button_clicked)
label.place(x = 100, y = 200)

input = Entry(width = 10)
text = input.get()
label.place(x = 100, y = 300)

window.mainloop()