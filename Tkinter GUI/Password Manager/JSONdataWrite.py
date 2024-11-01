from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def GenerateRandomPassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for l in range(randint(8, 10))]
    password_symbols = [choice(symbols) for s in range(randint(2, 4))]
    password_numbers = [choice(numbers) for n in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please enter your website and your password")
    else:
        correct = messagebox.askokcancel(title = "website", message = f"These are the details entered: \nUsername: {username} \nPassword: {password} \nEverything here correct?")
    if correct:
        with open("data.json", mode = "w") as file:
            #Write to a Json file
            json.dump(new_data, file, indent = 4)

            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text = "Website: ")
website_label.grid(column=0, row=1)

username_label = Label(text = "Email/Username: ")
username_label.grid(column=0, row=2)

password_label = Label(text = "Password: ")
password_label.grid(column=0, row=3)

#Inputs
website_input = Entry(width = 35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

username_input = Entry(width = 35)
username_input.grid(column=1, row=2, columnspan=2)
#username_input.insert(0,"seunojuoko@hotmail.com")

password_input = Entry(width = 21)
password_input.grid(column=1, row=3)

#Button
generate_button = Button(text = "Generate Password", command = GenerateRandomPassword)
generate_button.grid(column=2, row=3)

add_button = Button(text = "Add", width = 36, command = save)
add_button.grid(column=1, row=4)

window.mainloop()