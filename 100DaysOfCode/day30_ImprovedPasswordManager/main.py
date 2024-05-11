from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_numbers + password_letters + password_symbols

    random.shuffle(password_list)

    generated_password = "".join(password_list)

    password.insert(0, generated_password)
    pyperclip.copy(generated_password)
# -------------------------------- SEARCH ---------------------------------- #


def find_password():
    website_search = website.get().capitalize()
    try:
        with open("password_file.json", 'r') as password_file:
            data = json.load(password_file)
            password_search = data[website_search]['password']
            email_search = data[website_search]['email']
            pyperclip.copy(password_search)
            messagebox.showinfo(title=f"{website_search} Password",
                                message=f"   Email : {email_search}\n"
                                        f"Password : {password_search}\n"
                                        f"Password copied to clipboard.")
    except KeyError:
        messagebox.showinfo(title=f"{website_search} Password",
                            message=f"{website_search} does not have a recorded password.")
    except FileNotFoundError:
        messagebox.showinfo(title=f"Error",
                            message=f"No password file found.")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear():
    password.delete(0, 'end')
    website.delete(0, 'end')


def save():
    input_email = email.get()
    input_password = password.get()
    input_website = website.get().capitalize()
    new_data = {
        input_website: {
            "email": input_email,
            "password": input_password
        }
    }
    if len(input_email) == 0 or len(input_password) == 0:
        messagebox.showinfo(title="Missing info", message="You've left either the email or password empty")
    else:
        try:
            with open("password_file.json", 'r') as password_file:
                data = json.load(password_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("password_file.json", 'w') as password_file:
                json.dump(new_data, password_file, indent=4)
                clear()
        else:
            with open("password_file.json", 'w') as password_file:
                json.dump(data, password_file, indent=4)
        finally:
            clear()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

# Lock logo
canvas = Canvas(height=200, width=200, highlightthickness=0)
lock_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_photo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website")
email_label = Label(text="Email/Username")
password_label = Label(text="Password")

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# fill in text bars
website = Entry(width=33)
website.focus()
email = Entry(width=51)
email.insert(0, 'jameshark47@gmail.com')
password = Entry(width=33)

website.grid(column=1, row=1, columnspan=2, sticky='W')
email.grid(column=1, row=2, columnspan=2, sticky='W')
password.grid(column=1, row=3, sticky='W')

# Buttons
add_button = Button(text="Add", width=43, command=save)
generate_password_button = Button(text="Generate Password", command=generate_password)
search_button = Button(text="Search", width=14, command=find_password)

add_button.grid(column=1, row=4, columnspan=2, sticky='W')
generate_password_button.grid(column=2, row=3, sticky='W')
search_button.grid(column=2, row=1)

window.grid_columnconfigure(1, minsize=10)


window.mainloop()
