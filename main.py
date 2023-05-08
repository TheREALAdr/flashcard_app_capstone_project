from tkinter import *
from tkinter.ttk import *
from pandas import *


# ------------------------------ FLASHCARD GENERATION --------------------- #

with open(file=data/french_words.csv) as words_file:
    words_data = DataFrame(words_file)
    dict_of_words = words_data.to_dict(orient="records")
# ^^ Lines directly above should make a variable called "dict_of_words" 
#    that is a dictionary form of french_words.csv. You might want to make
#.   words_data only include the French side of french_words.csv later, but 
#.   run in an IDE later to check it out.
    

# ------------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# ------------------------------ USER INTERFACE ----------------------------- #

# Window Initialization
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas Initialization
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard = canvas.create_image(400, 263, image=card_front_image)
language = canvas.create_text(400, 150, text="Language", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))

# Images
card_front_image = PhotoImage(file="images/card_front.png")
red_x_image = PhotoImage(file="images/incorrect.png")
green_check_image = PhotoImage(file="images/correct.png")


# Buttons
unknown_button = Button(image=red_x_image, highlightthickness=0, activebackground=BACKGROUND_COLOR, borderwidth=0)
known_button = Button(image=green_check_image, highlightthickness=0, activebackground=BACKGROUND_COLOR, borderwidth=0)

# Adding elements to the grid
unknown_button.grid(column=0, row=1, sticky=EW)
known_button.grid(column=1, row=1, sticky=EW)
canvas.grid(column=0, row=0, columnspan=2)

window.mainloop()
