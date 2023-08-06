from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button, END, messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_random_password():
 
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    details = f"Website: {website}\nEmail: {email}\nPassword: {password}\n\n"
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Invalid Input", message="fields are empty")
    else:
        confirmation = messagebox.askokcancel(title="Confirm your input", message=f"are you sure to add the following details\n {details}")
        if confirmation:
            with open("data.txt", mode="a") as data:
                data.write(details)
            
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        
        messagebox.showinfo(title="Credentials Added Successfully", message="Account Added Successfully")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
image_value = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_value)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_entry = Entry(width=51)
website_entry.focus()
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2) 

email_label = Label(text="Email/Username:")
email_entry = Entry(width=51)
email_entry.insert(0, "sampleemail@mail.com")
email_label.grid(column=0, row=2)
email_entry.grid(column=1, row=2, columnspan=2) 

password_label = Label(text="Password:")
password_entry = Entry(width=32)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3) 

genrete_password_button = Button(text="Generate Password", command=generate_random_password)
genrete_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()