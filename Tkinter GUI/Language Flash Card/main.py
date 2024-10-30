from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
learn = {}

try:
    data = pandas.read_csv('data/french_words.csv')
except FileNotFoundError:
    original = pandas.read_csv('data/french_words.csv')
    learn = original.to_dict(orient='records')
else:
    learn = data.to_dict(orient='records')

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn)
    #print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill = "black")
    canvas.itemconfig(card_word, text=current_card["French"], fill = "black")
    canvas.itemconfig(card_background, image=front_card)
    window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill = "white")
    canvas.itemconfig(card_word, text=current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    learn.remove(current_card)
    #print(len(learn))
    data = pandas.DataFrame(learn)
    data.to_csv('data/french_words_to_learn.csv', index = False)
    next_card()

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(window, width=800, height=526)
front_card = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 236, image = front_card)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness = 0, command = is_known)
known_button.grid(row = 1, column = 1)

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness = 0, command = next_card)
unknown_button.grid(row = 1, column = 0)

next_card()

window.mainloop()

