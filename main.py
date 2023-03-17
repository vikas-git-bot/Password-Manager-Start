from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

    nr_letters = randint(8, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_lists = password_letters + password_numbers + password_symbols
    shuffle(password_lists)

    password = "".join(password_lists)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    w = web_entry.get()
    e = email_entry.get()
    p = pass_entry.get()

    if len(w) == 0 or len(p) == 0:
        messagebox.showerror(title="Oops!", message="Make sure you haven't left any empty fields")
    else:
        is_okay = messagebox.askyesno(title="Alert", message=f"These are the details \nWebsite: {w} \nEmail: {e} \n"
                                                             f"Password: {p}\nthe above information is correct?")
        if is_okay:
            with open("password_datafile.txt", mode="a") as df:
                df.write(f"{w}, {e}, {p} \n")

            web_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website", fg="Blue")
web_label.grid(row=1, column=0)
email_label = Label(text="Email", fg="Blue")
email_label.grid(row=2, column=0)
password_label = Label(text="Password", fg="Blue")
password_label.grid(row=3, column=0)

web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.insert(0, "vk2927538@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

password_gen_button = Button(text="Generate Password", command=generate_password)
password_gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
