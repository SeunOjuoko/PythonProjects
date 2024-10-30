import tkinter
from tkinter import Entry

window = tkinter.Tk()
window.title('Graphical User Interface (GUI)')
#Size of window
window.minsize(500, 300)

#Label
label = tkinter.Label(text='This is a Label', font=("Arial", 24, "bold"))
label.pack(expand = True)

def button_clicked():
    print("Button clicked")
    New_Text = input.get()
    label.config(text = New_Text)

button = tkinter.Button(text = "Click Me", command = button_clicked)
button.pack()

input = Entry(width = 10)
text = input.get()
input.pack()


window.mainloop()
  
