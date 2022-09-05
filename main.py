from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []

    alpha = [choice(letters) for x in range(randint(8,20))]
    symbols = [choice(symbols) for n in range(randint(2,4))]
    num = [choice(numbers) for z in range(randint(2,4))]

    password_list = alpha + symbols + num
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)





# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
            }

    if len(website) == 0 or password == 0:
        messagebox.showinfo(title="oops", message="Please Dont leave any fields empty!. ")
    else:

        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except(FileNotFoundError, json.decoder.JSONDecodeError):
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():

   get = website_entry.get()
   try:
       with open('data.json') as f:
           data_frame = json.load(f)
   except FileNotFoundError:
       messagebox.showinfo(title= "Error", message="No Data File Was Found")
   else:
       if get in data_frame:
           email = data_frame[get]["email"]
           password = data_frame[get]["password"]
           messagebox.showinfo(title=get, message=f"Email: {email}\nPassword: {password}")
       else:
           messagebox.showinfo(title="Error", message=f"No details for {get} was found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

label1 = Label(text="Website")
label1.grid(column=0, row=1)
label2 = Label(text="Email/Username: ")
label2.grid(column=0, row=2)
label3 = Label(text="Password: ")
label3.grid(column=0, row=3)


#Entries

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sameershaik556@gmail.com")
password_entry = Entry(width=28)
password_entry.grid(row=3, column=1)

#Buttons
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=3)
add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=5, column=1, columnspan=2)
search_button = Button(text="Search", width=15,command=find_password)
search_button.grid(column=3, row=1)

















window.mainloop()