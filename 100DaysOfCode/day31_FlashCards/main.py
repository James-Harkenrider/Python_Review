from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_TIMER = 3

current_card = {"german": None, "english": None}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    vocab_df = pandas.read_csv("./data/top100GermanWords.csv")
    to_learn = vocab_df.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    # [{german: word1, english:word1}, {german: word2, english:word2}, ..., {german: wordN, english:wordN}]
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfigure(card, image=card_front_img)
    canvas.itemconfigure(language_title, text="German", fill="black")
    canvas.itemconfigure(word_text, text=current_card["german"], fill="black")
    flip_timer = window.after(CARD_TIMER * 1000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfigure(language_title, text="English", fill="white")
    canvas.itemconfigure(word_text, text=current_card["english"], fill="white")
    canvas.itemconfigure(card, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    next_card()
    data_to_learn = pandas.DataFrame(to_learn)
    data_to_learn.to_csv("./data/words_to_learn.csv", index=False)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(CARD_TIMER * 1000, flip_card)

# Create canvas for card image
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)
language_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Add buttons to the window
cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
