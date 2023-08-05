from tkinter import Tk, Label, Entry, Button, Frame

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=500)
window.config(padx=60, pady=60)


miles = Label(text="MILES", font=("Morganite", 71, "bold"))
miles.place(x=0, y=0)

equal = Label(text="EQUAL TO", font=("Overpass", 10, "italic bold"))
equal.place(x=160, y=180)

answer = Label(text="12312", font=("Morganite", 100, "bold"))
answer.pack(side="bottom")
answer_width = answer.winfo_reqwidth()
km = Label(text="Km", font=("Morganite", 40, "bold"))
km.place(x=(200 + (answer_width / 2)), y=305)


border_color = Frame(window, background="red")

entry = Entry(width=18, font=("Morganite", 42, "bold"), highlightbackground="black", highlightthickness=6, justify="center")
entry.place(x=130, y=17)



def convert_input():
    user_input = float(entry.get())

    kilometer = user_input * 1.60934

    answer["text"] = kilometer
    answer_width = answer.winfo_reqwidth()
    km.place(x=(200 + (answer_width / 2)), y=305)


button = Button(text="CONVERT", font=("Overpass", 15, "bold"), background="black", foreground="white", width=31, command=convert_input)
button.place(x=0, y=100)



window.mainloop()