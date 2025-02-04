import json
from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password=""
    for i in range(random.randint(1,3)):
        password+=chr(random.randint(65,90))
    for i in range(random.randint(4,7)):
        password += chr(random.randint(97, 122))
    for i in range(random.randint(2,4)):
        password += str(random.randint(0,9))
    special_char=[37, 36, 35, 64, 38, 42]
    for i in range(random.randint(2,4)):
        password+=chr(random.choice(special_char))
    lst=list(password)
    random.shuffle(lst)
    password=''.join(lst)
    return password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file(website,username,password):
    new_data = {website: {"username": username, "password":password}}
    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        with open("data.json","w") as data_file:
            json.dump(new_data,data_file,indent=4)
    else:
        data.update(new_data)
        with open("data.json","w") as data_file:
            json.dump(data,data_file,indent=4)

# ---------------------------- UI SETUP ------------------------------- #

root=Tk()
root.title("Password-Manager")
root.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
pht_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pht_img)
canvas.grid(row=0,column=1,sticky="e")

website_label=Label(root,text="Website:")
website_label.grid(row=1,column=0)
website_entry=Entry(root,width=37)
website_entry.grid(row=1,column=1)
website_entry.focus()

username_label=Label(root,text="UserName:")
username_label.grid(row=2,column=0)
username_entry=Entry(root,width=53)
username_entry.grid(row=2,column=1,columnspan=2)

password_label=Label(root,text="Password:")
password_label.grid(row=3,column=0)
password_entry=Entry(root,width=37)
password_entry.grid(row=3,column=1,sticky="w")

def send_text():
    website=website_entry.get()
    username=username_entry.get()
    password=password_entry.get()

    option=messagebox.askyesno(title="Save Password",message=f"WEBSITE: {website}\nUSERNAME: {username}\nPASSWORD: {password}\n\n CONFIRM to save")
    if not option:
        return

    website_entry.delete(0,END)
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    website_entry.focus()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    save_to_file(website,username,password)

def insert_password():
    password=generate_password()
    password_entry.delete(0,END)
    password_entry.insert(0,password)

def search():
    website=website_entry.get()
    first_line=f"Website -- {website}"
    second_line=""
    third_line=""
    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)
            username=data[website]["username"]
            password=data[website]["password"]
    except FileNotFoundError:
        second_line="DATA NOT FOUND!!!"
    except KeyError:
        second_line="DATA NOT FOUND!!!"
    else:
        second_line=f"Username : {username}"
        third_line=f"Password  : {password}"
    messagebox.showinfo(title="Search Result",message=f"{first_line}\n{second_line}\n{third_line}")


search_button=Button(root,text="Search",width=12,command=search)
search_button.grid(row=1,column=2)

generate_button=Button(root,text="Generate",command=insert_password,width=12)
generate_button.grid(row=3,column=2,sticky="e")

add_button=Button(root,text="Add",width=45,command=send_text)
add_button.grid(row=4,column=1,columnspan=2)

root.mainloop()