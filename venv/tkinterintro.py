# from tkinter import *
#
# root = Tk()
#
# # #creating label widget
# # Label1=Label(root, text="Hello world")
# # Label1.pack()
#
#
#
# from tkinter import Image, ttk, messagebox, font
#
#
# def hello(a):
#     print(a)
#
# def hello2(event):
#     hello("Hello World!")
#
# login_button = Button(root, text="Login", bg="#77d5d2", width=20,command=lambda: hello("Hello World!"))
# login_button.bind("<Return>",hello2)
# login_button.focus()
# login_button.pack()
# root.mainloop()

# from tkinter import *
# import random
# import smtplib
#
# def send(user_email):
#     password = "Your ID password"
#
#     sender = "your Email ID"
#     receiver = user_email
#     random_number = random.randint(100000, 999999)
#
#     message = "Your OTP for confirming order is " + str(random_number)
#     subject = "Team CSEguy"
#
#     email = "subject: {} \n\n {}".format(subject, message)
#
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.ehlo()
#     s.starttls()
#
#     s.login(sender, password)
#
#     s.sendmail(sender, receiver, email)
#     print("email sent")
#     s.quit()
#
#
# root = Tk()
#
# email = Label(root, text="Email", bg="#8cfffb", padx=5, pady=5)
# email.grid(row=0, column=0, sticky=W, padx=7)
# email_entry = Entry(root, width=30)
# email_entry.grid(row=0, column=1)
#
# login_button = Button(root, text="Login", bg="#77d5d2",width=20,command=lambda: send(email_entry.get()))
# login_button.grid(row=1, column=0, columnspan=2, pady=10)
#


# root.mainloop()
# email = Label(root, text="Email", bg="#8cfffb", padx=5, pady=5)
# email.grid(row=0, column=0, sticky=W, padx=7)
# email_entry = Entry(root, width=30)
# email_entry.grid(row=0, column=1)
#
# password = Label(root, text="Password", bg="#8cfffb", padx=5, pady=5)
# password.grid(row=1, column=0, sticky=W, padx=7)
# password_entry = Entry(root, show="*", width=30)
# password_entry.grid(row=1, column=1)
#
# login_button = Button(root, text="Login", bg="#77d5d2",width=20)
# login_button.grid(row=2, column=0, columnspan=2, pady=10)


# cities = ["Ahmedabad", "Mumbai", "Delhi", "Bengaluru", "Rajkot", "Surat", "Chennai", "Pune", "Kolkata",
#               "Vadodara", "Valsad"]
# clicked = ttk.Combobox(root, value=cities, width=60)
# clicked.current(0)
# clicked.grid(row=1, column=1, sticky=W, pady=7, padx=7)

#
# address_entry = Text(root, height=5, width=46, padx=5, pady=5)
# address_entry.insert(1.0, "Address")
# address_entry.grid(row=0, column=1, pady=7, padx=7)


# c= IntVar()
#
#
# def hello(a):
#     print(a)
#
# Radiobutton(root, text="Cheese dip", bg="#e0ffff", variable=c,value=1).grid(row=2, column=0)
# Radiobutton(root, text="Peri Peri dip", bg="#e0ffff", variable=c,value=2).grid(row=3, column=0)
# button = Button(root, text="Enter", bg="#77d5d2", width=20,command=lambda: hello(c.get()))
# button.grid(row=4, column=0)

from tkinter import *
import sqlite3

# sign_up = Tk()
#
#
# def add_to_database():
#     conn = sqlite3.connect('input.db')
#     c = conn.cursor()
#
#     c.execute("""CREATE TABLE Customer_Info(
#         first_name text,
#         last_name text,
#         email text,
#         password text
#                     )""")
#
#     c.execute(
#         "insert into Customer_Info values (:first_name_entry_up,:last_name_entry_up,:email_entry_up,"
#         ":password_entry_up)",
#         {
#             'first_name_entry_up': first_name_entry_up.get(),
#             'last_name_entry_up': last_name_entry_up.get(),
#             'email_entry_up': email_entry_up.get(),
#             'password_entry_up': password_entry_up.get()
#         }
#     )
#
#     conn.commit()
#
#     conn.close()
#     print("data stored")
#
#
# first_name_up = Label(sign_up, text="First name", bg="#8cfffb", padx=5, pady=5)
# first_name_up.grid(row=0, column=0, sticky=W, padx=7)
# first_name_entry_up = Entry(sign_up)
# first_name_entry_up.grid(row=0, column=1)
#
# last_name_up = Label(sign_up, text="Last name", bg="#8cfffb", padx=5, pady=5)
# last_name_up.grid(row=1, column=0, sticky=W, padx=7)
# last_name_entry_up = Entry(sign_up)
# last_name_entry_up.grid(row=1, column=1)
#
# email_up = Label(sign_up, text="Email", bg="#8cfffb", padx=5, pady=5)
# email_up.grid(row=2, column=0, sticky=W, padx=7)
# email_entry_up = Entry(sign_up)
# email_entry_up.grid(row=2, column=1)
#
# password_up = Label(sign_up, text="Password", bg="#8cfffb", padx=5, pady=5)
# password_up.grid(row=3, column=0, sticky=W, padx=7)
# password_entry_up = Entry(sign_up, show="*")
# password_entry_up.grid(row=3, column=1)
#
# sign_up_button = Button(sign_up, text="Create account", bg="#77d5d2", width=20, padx=15, pady=15,
#                         command=add_to_database)
# sign_up_button.grid(row=5, column=0, columnspan=2, pady=20)
#
# sign_up.mainloop()

# from tkinter import *
# from tkinter import ttk
# import requests
#
# info_window = Tk()
#
#
# def OrderStatus():
#     Final_Window = Tk()
#     Final_Window.title("Order Status")
#
#     # Main Use of API key started from here
#     Api_key = "AIzaSyAF1_Dp4Z792oGtGDe3h9QM4uax6rCoOkE"
#
#     home = address_entry.get(1.0, END) + zipcode_entry.get() + "india"
#     destination = Restaurant_clicked.get()
#     url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + home + "&destinations=" + destination + "&key=" + Api_key
#     r = requests.get(url)
#     print(r.json())
#     time = r.json()["rows"][0]["elements"][0]["duration"]["value"]
#     time = int(int(time) / 60) + 15
#     time = "Estimated delivery time:" + str(time) + " min."
#     Label(Final_Window, text=time, bg="#e0ffff", font=myFont2).grid(row=1, column=0)
#
#     Final_Window.mainloop()
#
#
# address_label = Label(info_window, text="Address", bg="#8cfffb", padx=5, pady=5)
# address_label.grid(row=0, column=0, sticky=W + N, padx=7)
# address_entry = Text(info_window, height=5, width=46, padx=5, pady=5)
# address_entry.grid(row=0, column=1, pady=7, padx=7)
#
# city_label = Label(info_window, text="City", bg="#8cfffb", padx=5, pady=5)
# city_label.grid(row=1, column=0, sticky=W, padx=7)
# cities = ["City", "Ahmedabad", "Mumbai", "Delhi", "Bengaluru", "Rajkot", "Surat", "Chennai", "Pune", "Kolkata",
#           "Vadodara", "Valsad"]
# clicked = ttk.Combobox(info_window, value=cities, width=60)
# clicked.grid(row=1, column=1, sticky=W, pady=7, padx=7)
#
# zipcode_label = Label(info_window, text="Zipcode", bg="#8cfffb", padx=5, pady=5)
# zipcode_label.grid(row=2, column=0, sticky=W, padx=7)
# zipcode_entry = Entry(info_window, width=60)
# zipcode_entry.grid(row=2, column=1, pady=7, padx=7, sticky=W)
#
# Restaurant_label = Label(info_window, text="Select Restaurant", bg="#8cfffb", padx=5, pady=5)
# Restaurant_label.grid(row=3, column=0, sticky=W, padx=7)
# Restaurant_Name_List = ["Chocolate Room 380060", "Dominos Pizza 380060",
#                         "Lapinoz pizza 380060", "Mc. Donalds 380060", "Subway 380060"]
# Restaurant_clicked = ttk.Combobox(info_window, values=Restaurant_Name_List, width=60)
# Restaurant_clicked.grid(row=3, column=1, sticky=W, pady=7, padx=7)
#
# next = Button(info_window, text="Next", bg="#77d5d2", width=20, command=OrderStatus)
# next.grid(row=4, column=0, columnspan=2, pady=10)
# info_window.mainloop()

# import sqlite3
# from tkinter import *
# from tkinter import messagebox, ttk, font
#
# from PIL import ImageTk, Image
#
# import Application
#
# root = Tk()
# root.config(bg="#00ffff")
# a1 = Image.open("1.png")
# a1 = a1.resize((900, 480), Image.ANTIALIAS)
# a = ImageTk.PhotoImage(a1)
# image1 = Label(root, image=a)
# image1.place(x=0, y=0)
# root.geometry("900x480")
# root.title("Login Page")
# myFont = font.Font(size=20)
# myFont1 = font.Font(size=15)
#
#
# def sign_in_fun():
#     pass
#
#
# def sign_up_fun():
#     pass
#
#
# main_frame = LabelFrame(root, text="Login", bg="#11305b", font=myFont1, fg="#00a8f3")
# main_frame.grid(row=0, column=0, sticky=W + E, padx=300, pady=78)
#
# sign_in_button = Button(main_frame, text="Sign in", padx=40, pady=22, width=8, font=myFont, command=sign_in_fun)
# sign_in_button.grid(row=0, column=0, padx=50, pady=20)
#
# sign_up_button = Button(main_frame, text="Sign up", padx=40, pady=22, width=8, font=myFont, command=sign_up_fun)
# sign_up_button.grid(row=1, column=0, padx=50, pady=20)
#
# root.mainloop()
#
# def check_in_database():
#     conn = sqlite3.connect('data.db')
#
#     c = conn.cursor()
#     email = email_entry.get()
#     if email_entry.get() == "":
#         messagebox.showerror("Login status", "Email Empty")
#     elif password_entry.get() == "":
#         messagebox.showerror("Login status", "Password Empty")
#     else:
#
#         password = c.execute("select email,password from Customer_Info")
#         password = password.fetchall()
#         temp1 = (email_entry.get().lower(), password_entry.get())
#
#         if password.__contains__(temp1):
#             messagebox.showinfo("Login status", "Logged in successfully!")
#             root.destroy()
#             sign_in_window.destroy()
#             info(email)
#         else:
#             messagebox.showerror("Login status", "Invalid username or password")
#
#     conn.commit()
#
#     conn.close()
#
#
# def sign_in_fun():
#
#     global password_entry
#     global email_entry
#     global sign_in_window
#
#     sign_in_window = Tk()
#     sign_in_window.title("Sign In")
#     sign_in_window.config(bg="#8cfffb")
#
#     sign_in = LabelFrame(sign_in_window, text="Sign in", font=myFont2, bg="#8cfffb", padx=15, pady=15)
#     sign_in.grid(row=0, column=0, padx=20, pady=20)
#
#     email = Label(sign_in, text="Email", bg="#8cfffb", padx=5, pady=5, font=myFont1)
#     email.grid(row=0, column=0, sticky=W, padx=7)
#     email_entry = Entry(sign_in, font=myFont1, width=30)
#     email_entry.insert(0, "Email")
#     email_entry.grid(row=0, column=1)
#
#     password = Label(sign_in, text="Password", bg="#8cfffb", padx=5, pady=5, font=myFont1)
#     password.grid(row=1, column=0, sticky=W, padx=7)
#     password_entry = Entry(sign_in, show="*", font=myFont1, width=30)
#     password_entry.grid(row=1, column=1)
#
#     login_button = Button(sign_in, text="Login", bg="#77d5d2", font=myFont1, width=20, command=check_in_database)
#     login_button.grid(row=2, column=0, columnspan=2, pady=10)
#
#     sign_in_window.mainloop()

from tkinter import *
from tkinter import messagebox, ttk, font
#
# def add_to_database():
#     conn = sqlite3.connect('data.db')
#
#     c = conn.cursor()
#
#     # Execute only one time for creating database
#     # c.execute("""CREATE TABLE Customer_Info(
#     #     first_name text,
#     #     last_name text,
#     #     email text,
#     #     password text
#     #                 )""")
#
#     if first_name_entry_up.get() == "":
#         messagebox.showerror("Account Status", "First Name Empty")
#     elif last_name_entry_up.get() == "":
#         messagebox.showerror("Account Status", "Last Name Empty")
#     elif email_entry_up.get() == "":
#         messagebox.showerror("Account Status", "Email Empty")
#     elif password_entry_up.get() == "":
#         messagebox.showerror("Account Status", "Password Empty")
#     elif confirm_password_entry_up.get() == "":
#         messagebox.showerror("Account Status", "Password Empty")
#     elif confirm_password_entry_up.get() != password_entry_up.get():
#         messagebox.showerror("Account Status", "Password doesn't match")
#     else:
#         email = str(email_entry_up.get()).lower()
#         temp = (email,)
#         all_email = c.execute("select email from Customer_Info")
#         all_email = all_email.fetchall()
#
#         if email.__contains__("@"):
#             if all_email.__contains__(temp):
#                 messagebox.showerror("Account Status", "Email already exists.\nEnter a new one.")
#             else:
#                 c.execute(
#                     "insert into Customer_Info values (:first_name_entry_up,:last_name_entry_up,:email_entry_up,"
#                     ":password_entry_up)",
#                     {
#                         'first_name_entry_up': first_name_entry_up.get(),
#                         'last_name_entry_up': last_name_entry_up.get(),
#                         'email_entry_up': email_entry_up.get(),
#                         'password_entry_up': password_entry_up.get()
#                     }
#                 )
#                 messagebox.showinfo("Account Status", "Account Created")
#                 sign_up_window.destroy()
#
#         else:
#             messagebox.showerror("Account Status", "Enter a valid Email.")
#     conn.commit()
#
#     conn.close()
#
#
# def sign_up_fun():
#     # global sign_up_button
#     # sign_up_button.grid_forget()
#
#     global first_name_entry_up, sign_up_window, confirm_password_up, confirm_password_entry_up
#     global last_name_entry_up
#     global email_entry_up
#     global password_entry_up
#     global sign_up_window
#
#     def email_clear(event):
#         email_entry_up.delete(0, "end")
#
#     def first_clear(event):
#         first_name_entry_up.delete(0, "end")
#
#     def last_clear(event):
#         last_name_entry_up.delete(0, "end")
#
#     sign_up_window = Tk()
#     sign_up_window.title("Sign up")
#     sign_up_window.config(bg="#8cfffb")
#
#     sign_up = LabelFrame(sign_up_window, text="Sign up", bg="#8cfffb", padx=15, pady=15)
#     sign_up.grid(row=1, column=0, padx=20, pady=20)
#
#     first_name_up = Label(sign_up, text="First name", bg="#8cfffb", padx=5, pady=5)
#     first_name_up.grid(row=0, column=0, sticky=W, padx=7)
#     first_name_entry_up = Entry(sign_up)
#     first_name_entry_up.insert(0, "First_name")
#     first_name_entry_up.bind("<Button-1>", first_clear)
#     first_name_entry_up.grid(row=0, column=1)
#
#     last_name_up = Label(sign_up, text="Last name", bg="#8cfffb", padx=5, pady=5)
#     last_name_up.grid(row=1, column=0, sticky=W, padx=7)
#     last_name_entry_up = Entry(sign_up)
#     last_name_entry_up.insert(0, "Last Name")
#     last_name_entry_up.bind("<Button-1>", last_clear)
#     last_name_entry_up.grid(row=1, column=1)
#
#     email_up = Label(sign_up, text="Email", bg="#8cfffb", padx=5, pady=5)
#     email_up.grid(row=2, column=0, sticky=W, padx=7)
#     email_entry_up = Entry(sign_up)
#     email_entry_up.insert(0, "Email")
#     email_entry_up.bind("<Button-1>", email_clear)
#     email_entry_up.grid(row=2, column=1)
#
#     password_up = Label(sign_up, text="Password", bg="#8cfffb", padx=5, pady=5)
#     password_up.grid(row=3, column=0, sticky=W, padx=7)
#     password_entry_up = Entry(sign_up, show="*")
#     password_entry_up.grid(row=3, column=1)
#
#     confirm_password_up = Label(sign_up, text="Confirm Password", bg="#8cfffb", padx=5, pady=5)
#     confirm_password_up.grid(row=4, column=0, sticky=W, padx=7)
#     confirm_password_entry_up = Entry(sign_up, show="*")
#     confirm_password_entry_up.grid(row=4, column=1)
#
#     sign_up_button = Button(sign_up, text="Create account", bg="#77d5d2", width=20, padx=15, pady=15,
#                             command=add_to_database)
#     sign_up_button.grid(row=5, column=0, columnspan=2, pady=20)
#
#     sign_up_window.mainloop()
#
# sign_up_fun()

import Application
def  get_info(email):
    info_dict = {'email': email, 'City': clicked.get(), 'Address': address_entry.get(1.0, END),
                 'Zipcode': zipcode_entry.get()}
    info_window.destroy()
    application()


def info(email):
    global info_window
    info_window = Tk()
    info_window.title("Delivery Information")
    info_window.config(bg="#8cfffb")

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
            get_info(email)

    city_label = Label(info_window, text="City", bg="#8cfffb", padx=5, pady=5)
    city_label.grid(row=1, column=0, sticky=W, padx=7)
    cities = ["City", "Ahmedabad", "Mumbai", "Delhi", "Bengaluru", "Rajkot", "Surat", "Chennai", "Pune", "Kolkata",
              "Vadodara", "Valsad"]
    clicked = ttk.Combobox(info_window, value=cities, width=60)
    clicked.current(0)
    clicked.grid(row=1, column=1, sticky=W, pady=7, padx=7)

    address_label = Label(info_window, text="Address", bg="#8cfffb", padx=5, pady=5)
    address_label.grid(row=0, column=0, sticky=W + N, padx=7)
    address_entry = Text(info_window, height=5, width=46, padx=5, pady=5)
    address_entry.insert(1.0, "Address")
    address_entry.bind("<Button-1>", address_clear)
    address_entry.grid(row=0, column=1, pady=7, padx=7)

    zipcode_label = Label(info_window, text="Zipcode", bg="#8cfffb", padx=5, pady=5)
    zipcode_label.grid(row=2, column=0, sticky=W, padx=7)
    zipcode_entry = Entry(info_window, width=60)
    zipcode_entry.insert(0, "Zipcode")
    zipcode_entry.bind("<Button-1>", zipcode_clear)

    def zipcode_enter(event):
        check_entries()

    zipcode_entry.bind("<Return>", zipcode_enter)
    zipcode_entry.grid(row=2, column=1, pady=7, padx=7, sticky=W)

    next = Button(info_window, text="Next", bg="#77d5d2", width=20, command=check_entries)
    next.grid(row=4, column=0, columnspan=2, pady=10)

    info_window.mainloop()

info("skfhdjkf")