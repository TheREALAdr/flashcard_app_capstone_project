from tkinter import *
from tkinter.ttk import *


# ------------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ------------------------------ USER INTERFACE ----------------------------- #

# Window Initialization
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)

# Canvas Initialization
canvas = Canvas(width=800, height=526, highlightthickness=)
canvas.create_image(400, 263, image=card_front.png)
# ^ Add keywords for the first two numbers? Hard to understand if
# you don't know how canvas.create_image(kw**) works.
canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
canvas.create_text(400, 263, text="Title", font=(FONT_NAME, 60, "bold"))

# Images
card_front = PhotoImage(file="images/card_front.png")
incorrect_image = PhotoImage(file="images/incorrect.png")
correct_image = PhotoImage(file="images/correct.png")


# Buttons
incorrect_button = Button(image=incorrect_image, highlightthickness=0)
correct_button = Button(image=correct_image, highlightthickness=0)

# Padding
incorrect_image.grid(column=0, row=1)
correct_image.grid(column=1, row=1)
canvas.grid
#Ending here, need to finish the gridding and keywords for the canvas. Might do that later.
