from json import JSONDecodeError
from tkinter import *
import random
from tkinter import messagebox
import json

all_chars = [
    # Lowercase letters
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',

    # Uppercase letters
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',

    # Numbers
    '0','1','2','3','4','5','6','7','8','9',

    # Symbols (printable ASCII)
    '!','"','#','$','%','&',"'",'(',')','*','+',
    ',', '-', '.', '/', ':',';','<','=','>','?',
    '@','[',']','^','_','`','{','|','}','~'
]

def add_pass():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {website:{
        "email": email,
        "password": password
    }}
    if website == "" or password == "":
        messagebox.showerror("Error", "Please enter all required information")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        #file does not exist
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        #file is empty
        except JSONDecodeError:
            data = new_data
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)



def search():
    website = website_entry.get()
    print(type(website))
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo("Password Manager", f"Username:,{email}\nPassword:{password}")
    except FileNotFoundError:
        messagebox.showerror("Error", "No passwords are stored.")
    except KeyError:
        messagebox.showerror("Error", "No credentials are stored for this website.")


def generate_pass():
    pass_entry.delete(0, END)
    generated_pass = ""
    for x in range(0, 16):
        generated_pass += random.choice(all_chars)
    pass_entry.insert(END, generated_pass)



window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
window.attributes("-topmost", True)
window.focus_force()
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(window, text="Website")
website_label.grid(row=1, column=0)
email_label = Label(window, text="Email")
email_label.grid(row=2, column=0)
pass_label = Label(window, text="Password")
pass_label.grid(row=3, column=0)

website_entry = Entry(width=20)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "alex@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width=20)
pass_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", width=11, command=generate_pass)
generate_password_button.grid(row=3, column=2)
add_password_button = Button(text="Add Password", width=33, command=add_pass)
add_password_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=11, command=search)
search_button.grid(row=1, column=2, columnspan=1)













window.mainloop()