from tkinter import Tk, Button, PhotoImage, Canvas
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

data = {}
current_word = {}
def read_progress_file():
    global data
    try:
        progress_data = pandas.read_csv("./data/words_to_learn.csv").to_dict()
        data = progress_data
        print(len(data["English"]), len(data["French"]))
    except FileNotFoundError:
        default_file = pandas.read_csv("./data/french_words.csv").to_dict()
        data = default_file

def save_progress():
    global data, current_word
   
    french_data = [value for (_, value) in data["French"].items()]
    english_data = [value for (_, value) in data["English"].items()]
    # print(f"FRENCH {french_data}\n\n")
    # print(f"English {english_data}")

    french_data.remove(current_word["French"])
    english_data.remove(current_word["English"])
    
    # print(len(french_data), len(english_data))
    
    updated_progress_data = {
        "French":  french_data,
        "English": english_data
    }
    df = pandas.DataFrame(updated_progress_data)
    df.to_csv("./data/words_to_learn.csv")
    new_card()

def generate_random_word():
    global current_word, data
    read_progress_file()
    try:
        random_key = random.choice(list(data["French"].keys()))
    except IndexError:
        default_file = pandas.read_csv("./data/french_words.csv").to_dict()
        data = default_file
        random_key = random.choice(list(data["French"].keys()))

    french_word =  data["French"][random_key]
    english_equivalent = data["English"][random_key]

    current_word = {"French" : french_word, "English" : english_equivalent, "Key": random_key}
    return french_word

def new_card():
    global flip_card
    window.after_cancel(flip_card)
    new_word = generate_random_word()
    canvas.itemconfig(word, text=new_word)
    canvas.itemconfig(flash_card, image=front_flash_card_image)
    canvas.itemconfig(language, fill="black", text="French")
    canvas.itemconfig(word, fill="black")
    flip_card = window.after(3000, turn_card)


def turn_card():
    canvas.itemconfig(flash_card, image=back_flash_card_image)
    canvas.itemconfig(language, fill="white", text="English")
    canvas.itemconfig(word, fill="white", text=current_word["English"])


window = Tk()
window.title("Flash Card App Capstone Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

check_button_image = PhotoImage(file="./images/right.png")
cross_button_image = PhotoImage(file="./images/wrong.png")
front_flash_card_image = PhotoImage(file="./images/card_front.png")
back_flash_card_image = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card = canvas.create_image(400, 263, image=front_flash_card_image)
language = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT)
word = canvas.create_text(400, 263, text=generate_random_word(), font=WORD_FONT)

check_button = Button(image=check_button_image, borderwidth=0, highlightthickness=0, command=save_progress)
cross_button = Button(image=cross_button_image, borderwidth=0, highlightthickness=0, command=new_card)

canvas.grid(column=0, row=1, columnspan=2)
check_button.grid(column=1, row=2)
cross_button.grid(column=0, row=2)

flip_card = window.after(3000, turn_card)

window.mainloop()