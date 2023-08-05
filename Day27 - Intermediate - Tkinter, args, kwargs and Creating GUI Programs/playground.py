from tkinter import *


#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)


#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(column=1, row=1)


#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.grid(column=4, row=3)


#Buttons
button = Button(text="Click Me")
button.grid(column=2, row=2)


#Buttons
new_button = Button(text="Click Me")
new_button.grid(column=3, row=1)

window.mainloop()