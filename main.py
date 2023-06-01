from tkinter import *
import pandas
import random
import csv

# This project currently only works with French and English. Later on, see if you can add
# functionality that lets you grab 100 most popular words of ANY language from
# Wikipedia once a user types a valid language they want to learn. After that, 
# it should be converted to a .CSV and be ready for use with this program.
# Challenge is yours for the taking. You up?

# ------------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# ------------------------------ WORD GENERATION --------------------- #

with open(file="data/french_words.csv") as words_file:
    words_data = pandas.read_csv(words_file)
    dict_of_words = words_data.to_dict(orient="records")

current_word = {}


def generate_words():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(dict_of_words)
    next_word()
    flip_timer = window.after(3000, flip_card)


# Moving to another card
def next_word():
    foreign_translation = current_word["French"]
    canvas.itemconfig(flashcard, image=card_front_image)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=f"{foreign_translation}", fill="black")


# Flipping the current card
def flip_card():
    canvas.itemconfig(flashcard, image=card_back_image)
    known_translation = current_word['English']
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=f"{known_translation}", fill="white")


# ------------------------------ REMOVING WORDS/ADDING TO OTHER FILES --------------------- #
def generate_and_remove_words():
    try:
        dict_of_words.remove(current_word)
        words_to_learn = pandas.DataFrame(data=dict_of_words)
        words_to_learn.to_csv("words_to_learn.csv", index=False)
        # Might be a simpler way to do this, check the pandas.Dataframe.to_csv() method later.
    except ValueError:
        pass
    # except FileNotFoundError:
    #     words_to_learn_file = open("words_to_learn.csv", mode="w")
    #     with open("words_to_learn.csv", mode="a") as words_to_learn_file:
    #         words_to_learn_file.write(f"\n{current_word}")
    finally:
        generate_words()


# ------------------------------ USER INTERFACE/VARIABLES ----------------------------- #

# Window Initialization
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flip Timer Variable
flip_timer = window.after(3000, flip_card)

# Images
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
red_x_image = PhotoImage(file="images/incorrect.png")
green_check_image = PhotoImage(file="images/correct.png")

# Canvas Initialization
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard = canvas.create_image(400, 263, image=card_front_image)
language = canvas.create_text(400, 150, text="Language", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))

# Buttons
unknown_button = Button(image=red_x_image, command=generate_words, bg=BACKGROUND_COLOR,
                        activebackground=BACKGROUND_COLOR, highlightthickness=0, bd=0, )
known_button = Button(image=green_check_image, command=generate_and_remove_words, bg=BACKGROUND_COLOR,
                      activebackground=BACKGROUND_COLOR,
                      highlightthickness=0, bd=0)

# Adding elements to the grid
unknown_button.grid(column=0, row=1, sticky=EW)
known_button.grid(column=1, row=1, sticky=EW)
canvas.grid(column=0, row=0, columnspan=2)

window.mainloop()
