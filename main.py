from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    final_list = []

    letter_list = [final_list.append(random.choice(letters)) for char in range(nr_letters)]


    number_list = [final_list.append(random.choice(numbers)) for char in range(nr_numbers)]


    symbol_list = [final_list.append(random.choice(symbols)) for char in range(nr_symbols)]

    
    random.shuffle(final_list)

    password = ""


    for char in final_list:
        password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    web_info = web_entry.get().title()

    email_info = email_entry.get()
    password_info = password_entry.get()

    new_data_dictionary = {
         web_info : {
            "Email": email_info, 
            "Password" : password_info
        }
    }

    

    
    if len(web_info) == 0:
        messagebox.showerror(title="Empty Field", message=f"The Website field is empty, please try again")
        
    elif len(password_info) == 0:
    
        messagebox.showerror(title="Empty Field", message=f"The Password field is empty, please try again")
        
    elif len(web_info) > 0 and len(password_info) > 0:

        confirmation = messagebox.askyesno(title="Submit info", message=f"Are these details correct?\n Email: {email_info}\n Website: {web_info}\n Password: {password_info}")
    
        if confirmation == True:
            try:
                data_file = open("saved_file.json", "r")
            except FileNotFoundError:
                data_file = open("saved_file.json", "w")
                json.dump(new_data_dictionary, data_file, indent=4)
            else:
                py_data = json.load(data_file)
                new_data_dictionary.update(py_data)

                data_file = open("saved_file.json", "w")
                json.dump(new_data_dictionary, data_file, indent=4)

               
                    
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            data_file.close()
            messagebox.showinfo(title="Success!",message="Your data has beeen added successfully")



# ---------------------------- PASSWORD SEARCH FUNCTIONALITY ------------------------------- #
            
def find_password():
    web_search = web_entry.get().title()
    
    

    try:
        data_file = open("saved_file.json","r")

    except KeyError:
        messagebox.showinfo(title="Data Error", message="Sorry that data doesn't exist")
         


    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
        
        
    else:
        py_data = json.load(data_file)
    
        if web_search.title() in py_data:
            
            email = py_data[web_search]["Email"]
            password = py_data[web_search]["Password"]

            messagebox.showinfo(title=f"{web_search.title()}", message=f"Email: {email} Password: {password}")
            
        else:
            messagebox.showinfo(title="Error", message=f"Sorry there are no results for your search: [{web_search.title()}]")

            
                

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()

screen.title("Password Generator")
screen.config(background="white", padx=50, pady=50)            

logo = PhotoImage(file="logo.png")

my_canvas = Canvas(height=200, width=200, bg="white", highlightbackground="white")
my_canvas.grid(row=0, column=1)

my_canvas.create_image(125,100, image=logo)

web_label = Label(text="Website:", background="white")
web_label.grid(row=1, column=0)

web_entry = Entry(width=24, highlightcolor="blue")
web_entry.place(x=119,y=199)


email_label = Label(text="Email/Username:", background="white")
email_label.grid(row=2, column=0)


email_entry = Entry(width=43, highlightcolor="blue")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "Paulq10@gmail.com")

password_label = Label(text="Password:", background="white")
password_label.grid(row=3, column=0)

password_entry = Entry(width=24, highlightcolor="blue")
password_entry.place(x=119, y=248)

gen_pass_button = Button(background="white", text="Generate Password", pady=0, width=15, command=random_password)
gen_pass_button.place(x=320, y=248)


add_button = Button(text="Add", background="white", width=40, pady=0, command=save_info)
add_button.place(x=119, y=272)

search_button = Button(text="Search", width=15, bg="white", pady=0, command=find_password)
search_button.place(x=320, y=199)





screen.mainloop()