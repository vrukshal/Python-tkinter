import sqlite3
from tkinter import *
from tkinter import messagebox, ttk, font

from dotenv import load_dotenv

load_dotenv()

from PIL import ImageTk, Image

import Application



root = Tk()
root.config(bg="#00ffff")
a1 = Image.open("GUI/1.png")
a1 = a1.resize((900, 480), Image.ANTIALIAS)
a = ImageTk.PhotoImage(a1)
image1 = Label(root, image=a)
image1.place(x=0, y=0)
root.geometry("900x480")
root.title("Login Page")
myFont = font.Font(size=20)
myFont1 = font.Font(size=15)
myFont2 = font.Font(size=13)


# root.geometry("400x400")


def application(email):
    info_dict = {'email': email, 'City': clicked.get(), 'Address': address_entry.get(1.0, END),
                 'Zipcode': zipcode_entry.get()}
    info_window.destroy()
    Application.info(info_dict)
    Application.application()


def info(email):
    global info_window
    info_window = Tk()
    info_window.title("Delivery Information")
    info_window.config(bg="#8cfffb")
    info_window.after(1, lambda: info_window.focus_force())

    global clicked
    global address_entry
    global zipcode_entry

    def address_clear(event):
        address_entry.delete(1.0, "end")

    def zipcode_clear(event):
        zipcode_entry.delete(0, "end")

    def check_entries():
        if clicked.get() == "City":
            messagebox.showerror("Address status", "Choose a city")
        elif address_entry.get(1.0, END).strip() == "Address" or address_entry.get(1.0, END).strip() == "":
            messagebox.showerror("Address status", "Address field empty")
        elif (zipcode_entry.get()).isnumeric() == FALSE or len(zipcode_entry.get()) != 6 or zipcode_entry.get() == "":
            messagebox.showerror("Address status", "Invalid zipcode")
        else:
            application(email)

    city_label = Label(info_window, text="City", bg="#8cfffb", padx=5, pady=5, font=myFont1)
    city_label.grid(row=1, column=0, sticky=W, padx=7)
    cities = ["City", "Ahmedabad", "Mumbai", "Delhi", "Bengaluru", "Rajkot", "Surat", "Chennai", "Pune", "Kolkata",
              "Vadodara", "Valsad"]
    clicked = ttk.Combobox(info_window, value=cities, width=60)
    clicked.current(0)
    clicked.grid(row=1, column=1, sticky=W, pady=7, padx=7)

    address_label = Label(info_window, text="Address", bg="#8cfffb", padx=5, pady=5, font=myFont1)
    address_label.grid(row=0, column=0, sticky=W + N, padx=7)
    address_entry = Text(info_window, height=5, width=46, padx=5, pady=5)
    address_entry.insert(1.0, "Address")
    address_entry.bind("<Button-1>", address_clear)
    address_entry.grid(row=0, column=1, pady=7, padx=7)

    zipcode_label = Label(info_window, text="Zipcode", bg="#8cfffb", padx=5, pady=5, font=myFont1)
    zipcode_label.grid(row=2, column=0, sticky=W, padx=7)
    zipcode_entry = Entry(info_window, width=60)
    zipcode_entry.insert(0, "Zipcode")
    zipcode_entry.bind("<Button-1>", zipcode_clear)

    def zipcode_enter(event):
        check_entries()

    zipcode_entry.bind("<Return>", zipcode_enter)
    zipcode_entry.grid(row=2, column=1, pady=7, padx=7, sticky=W)

    next = Button(info_window, text="Next", bg="#77d5d2", font=myFont1, width=20, command=check_entries)
    next.grid(row=4, column=0, columnspan=2, pady=10)

    info_window.mainloop()


def check_in_database():
    conn = sqlite3.connect('data.db')

    c = conn.cursor()
    email = email_entry.get()
    if email_entry.get() == "":
        messagebox.showerror("Login status", "Email Empty")
    elif password_entry.get() == "":
        messagebox.showerror("Login status", "Password Empty")
    else:

        password = c.execute("select email,password from Customer_Info")
        password = password.fetchall()
        temp1 = (email_entry.get().lower(), password_entry.get())

        if password.__contains__(temp1):
            messagebox.showinfo("Login status", "Logged in successfully!")
            root.destroy()
            sign_in_window.destroy()
            info(email)
        else:
            messagebox.showerror("Login status", "Invalid username or password")

    conn.commit()

    conn.close()


def add_to_database():
    conn = sqlite3.connect('data.db')

    c = conn.cursor()

    # c.execute("""CREATE TABLE Customer_Info(
    #     first_name text,
    #     last_name text,
    #     email text,
    #     password text
    #                 )""")

    if first_name_entry_up.get() == "":
        messagebox.showerror("Account Status", "First Name Empty")
    elif last_name_entry_up.get() == "":
        messagebox.showerror("Account Status", "Last Name Empty")
    elif email_entry_up.get() == "":
        messagebox.showerror("Account Status", "Email Empty")
    elif password_entry_up.get() == "":
        messagebox.showerror("Account Status", "Password Empty")
    elif confirm_password_entry_up.get() == "":
        messagebox.showerror("Account Status", "Password Empty")
    elif confirm_password_entry_up.get() != password_entry_up.get():
        messagebox.showerror("Account Status", "Password doesn't match")
    else:
        email = str(email_entry_up.get()).lower()
        temp = (email,)
        all_email = c.execute("select email from Customer_Info")
        all_email = all_email.fetchall()

        if email.__contains__("@"):
            if all_email.__contains__(temp):
                messagebox.showerror("Account Status", "Email already exists.\nEnter a new one.")
            else:
                c.execute(
                    "insert into Customer_Info values (:first_name_entry_up,:last_name_entry_up,:email_entry_up,"
                    ":password_entry_up)",
                    {
                        'first_name_entry_up': first_name_entry_up.get(),
                        'last_name_entry_up': last_name_entry_up.get(),
                        'email_entry_up': email_entry_up.get(),
                        'password_entry_up': password_entry_up.get()
                    }
                )
                messagebox.showinfo("Account Status", "Account Created")
                sign_up_window.destroy()

        else:
            messagebox.showerror("Account Status", "Enter a valid Email.")
    conn.commit()

    conn.close()


def sign_in_fun():
    # global sign_in_button
    # sign_in_button.grid_forget()

    global password_entry
    global email_entry
    global sign_in_window

    sign_in_window = Tk()
    sign_in_window.title("Sign In")
    sign_in_window.config(bg="#8cfffb")
    sign_in_window.after(1, lambda: sign_in_window.focus_force())

    def email_clear(event):
        email_entry.delete(0, "end")

    sign_in = LabelFrame(sign_in_window, text="Sign in", font=myFont2, bg="#8cfffb", padx=15, pady=15)
    sign_in.grid(row=0, column=0, padx=20, pady=20)

    email = Label(sign_in, text="Email", bg="#8cfffb", padx=5, pady=5, font=myFont1)
    email.grid(row=0, column=0, sticky=W, padx=7)
    email_entry = Entry(sign_in, font=myFont1, width=30)
    email_entry.insert(0, "Email")
    email_entry.bind("<Button-1>", email_clear)

    def email_enter(event):
        password_entry.focus()

    email_entry.bind("<Return>", email_enter)
    email_entry.grid(row=0, column=1)
    email_entry.focus()

    password = Label(sign_in, text="Password", bg="#8cfffb", padx=5, pady=5, font=myFont1)
    password.grid(row=1, column=0, sticky=W, padx=7)
    password_entry = Entry(sign_in, show="*", font=myFont1, width=30)
    password_entry.grid(row=1, column=1)

    def password_enter(event):
        check_in_database()

    password_entry.bind("<Return>", password_enter)

    login_button = Button(sign_in, text="Login", bg="#77d5d2", font=myFont1, width=20, command=check_in_database)
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def login_enter(event):
        check_in_database()

    login_button.bind("<Return>", login_enter)

    sign_in_window.mainloop()


def sign_up_fun():
    # global sign_up_button
    # sign_up_button.grid_forget()

    global first_name_entry_up, sign_up_window, confirm_password_up, confirm_password_entry_up
    global last_name_entry_up
    global email_entry_up
    global password_entry_up
    global sign_up_window

    def email_clear(event):
        email_entry_up.delete(0, "end")

    def first_clear(event):
        first_name_entry_up.delete(0, "end")

    def last_clear(event):
        last_name_entry_up.delete(0, "end")

    sign_up_window = Tk()
    sign_up_window.title("Sign up")
    sign_up_window.config(bg="#8cfffb")
    sign_up_window.after(1, lambda: sign_up_window.focus_force())

    sign_up = LabelFrame(sign_up_window, text="Sign up", font=myFont2, bg="#8cfffb", padx=15, pady=15)
    sign_up.grid(row=1, column=0, padx=20, pady=20)

    first_name_up = Label(sign_up, text="First name", font=myFont1, bg="#8cfffb", padx=5, pady=5)
    first_name_up.grid(row=0, column=0, sticky=W, padx=7)
    first_name_entry_up = Entry(sign_up, font=myFont1)
    first_name_entry_up.insert(0, "First_name")
    first_name_entry_up.bind("<Button-1>", first_clear)

    def first_enter(event):
        last_name_entry_up.focus()

    first_name_entry_up.bind("<Return>", first_enter)
    first_name_entry_up.grid(row=0, column=1)
    first_name_entry_up.focus()

    last_name_up = Label(sign_up, text="Last name", font=myFont1, bg="#8cfffb", padx=5, pady=5)
    last_name_up.grid(row=1, column=0, sticky=W, padx=7)
    last_name_entry_up = Entry(sign_up, font=myFont1)
    last_name_entry_up.insert(0, "Last Name")
    last_name_entry_up.bind("<Button-1>", last_clear)

    def last_enter(event):
        email_entry_up.focus()

    last_name_entry_up.bind("<Return>", last_enter)
    last_name_entry_up.grid(row=1, column=1)

    email_up = Label(sign_up, text="Email", font=myFont1, bg="#8cfffb", padx=5, pady=5)
    email_up.grid(row=2, column=0, sticky=W, padx=7)
    email_entry_up = Entry(sign_up, font=myFont1)
    email_entry_up.insert(0, "Email")
    email_entry_up.bind("<Button-1>", email_clear)

    def email_enter(event):
        password_entry_up.focus()

    email_entry_up.bind("<Return>", email_enter)
    email_entry_up.grid(row=2, column=1)

    password_up = Label(sign_up, text="Password", font=myFont1, bg="#8cfffb", padx=5, pady=5)
    password_up.grid(row=3, column=0, sticky=W, padx=7)
    password_entry_up = Entry(sign_up, show="*", font=myFont1)

    def password_enter(event):
        confirm_password_entry_up.focus()

    password_entry_up.bind("<Return>", password_enter)
    password_entry_up.grid(row=3, column=1)

    confirm_password_up = Label(sign_up, text="Confirm Password", font=myFont1, bg="#8cfffb", padx=5, pady=5)
    confirm_password_up.grid(row=4, column=0, sticky=W, padx=7)
    confirm_password_entry_up = Entry(sign_up, show="*", font=myFont1)

    def confirm_password_enter(event):
        add_to_database()

    confirm_password_entry_up.bind("<Return>", confirm_password_enter)
    confirm_password_entry_up.grid(row=4, column=1)

    sign_up_button = Button(sign_up, text="Create account", font=myFont1, bg="#77d5d2", width=20, padx=15, pady=15,
                            command=add_to_database)
    sign_up_button.grid(row=5, column=0, columnspan=2, pady=20)

    def sign_up_enter(event):
        add_to_database()

    sign_up_button.bind("<Return>", sign_up_enter)

    sign_up_window.mainloop()


def sign_in_enter(event):
    sign_in_fun()


def sign_up_enter(event):
    sign_up_fun()


main_frame = LabelFrame(root, text="Login", bg="#11305b", font=myFont1, fg="#00a8f3")
main_frame.grid(row=0, column=0, sticky=W + E, padx=300, pady=78)

sign_in_button = Button(main_frame, text="Sign in", padx=40, pady=22, width=8, font=myFont, command=sign_in_fun)
sign_in_button.grid(row=0, column=0, padx=50, pady=20)
sign_in_button.focus_set()
sign_in_button.bind("<Return>", sign_in_enter)

sign_up_button = Button(main_frame, text="Sign up", padx=40, pady=22, width=8, font=myFont, command=sign_up_fun)
sign_up_button.grid(row=1, column=0, padx=50, pady=20)
sign_up_button.bind("<Return>", sign_up_enter)

root.mainloop()
