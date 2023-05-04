from tkinter import *
from tkinter.ttk import *


# ------------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ------------------------------ USER INTERFACE ----------------------------- #

# Window Initialization
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas Initialization
canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.create_image(400, 263, image=card_front.png)
title = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))

# Images
card_front = PhotoImage(file="images/card_front.png")
incorrect_image = PhotoImage(file="images/incorrect.png")
correct_image = PhotoImage(file="images/correct.png")


# Buttons
incorrect_button = Button(image=incorrect_image, highlightthickness=0)
correct_button = Button(image=correct_image, highlightthickness=0)

# Adding elements to the grid
incorrect_button.grid(column=0, row=1, sticky=EW)
correct_button.grid(column=1, row=1, sticky=EW)
canvas.grid(column=0, row=0, columnspan=2)
