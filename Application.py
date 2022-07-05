import os
import random
import smtplib
import sqlite3
import time
from tkinter import *
from tkinter import Image, ttk, messagebox, font

from PIL import ImageTk, Image
import requests
import smtplib
import json

row_index = 1
cart_list = []
total_price = 0

def final(user_email):
    global restaurant_index_1, info_dict
    Pay_window.destroy()
    Final_Window = Tk()
    Final_Window.title("Order Status")
    Final_Window.config(bg="#e0ffff")

    Label(Final_Window, text="Order Placed", bg="#e0ffff", font=myFont2).grid(row=0, column=0)
    Label(Final_Window, text="Thank you for ordering with us.", bg="#e0ffff", font=myFont2).grid(row=2, column=0)

    Api_key = os.getenv("API_KEY")
    home = info_dict["Address"] + info_dict["Zipcode"] +"Gujrat"+"india"
    destination = Restaurant_Name_List[restaurant_index_1]
    #print(destination)
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + home + "&destinations=" + destination + "&key=" + Api_key
    #print(url)
    r = requests.get(url)
    print(r.json())
    time = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    time = int(int(time)/60) + 15
    time = "Estimated delivery time:"+str(time)+" min."
    Label(Final_Window, text=time, bg="#e0ffff", font=myFont2).grid(row=1, column=0)
    dest=r.json()["destination_addresses"]
    hom=r.json()["origin_addresses"]
    #print(hom[0])
    #print(dest[0])

    distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]
    #print("\n the total time is", time)
    #photo of the path
    API_KEY = os.getenv("API_KEY")


    ZOOM = 14

    URL = "https://maps.googleapis.com/maps/api/staticmap?center=&zoom=12&size=2000x2000&maptype=roadmap&markers=color:red%7Clabel:C%7C23.0225,72.5714&path=color:0xff0000ff|weight:5""| "+home+"|"+destination+"&key="+ API_KEY
    #print(URL)
    response = requests.get(URL)

    with open('path.jpg', 'wb') as file:
        file.write(response.content)

    a12 = Image.open("path.jpg")
    #a12 = a12.resize((500, 500), Image.ANTIALIAS)
    a3 = ImageTk.PhotoImage(a12)
    Label(Final_Window,image=a3, bg="#e0ffff", font=myFont2).grid(row=3, column=0)
    #end of path
    sender = os.getenv("sender")
    receiver = user_email
    password = os.getenv("password")

    message = "Your order has been confirmed.\n"+time+"\nTeam TTE"
    subject = "Order Status"

    email = "subject: {} \n\n {}".format(subject, message)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.login(sender, password)
    s.sendmail(sender, receiver, email)
    s.quit()


    # try:
    #     t = 5
    #     while t:
    #         Final_Window.update()
    #         time.sleep(1)
    #         t -= 1
    #         if t == 0:
    #             Final_Window.destroy()
    #             os.system("python main.py")
    #             break
    # except:
    #     pass
    Final_Window.mainloop()


def pay(index, user_email):
    if index == 2 or index == 3 or index == 4:
        Checkout_Window.destroy()
    else:
        messagebox.showerror("Error", "Select payment method.")
        return
    global random_number, Pay_window
    Pay_window = Tk()
    Pay_window.title("Confirmation")
    Pay_window.config(bg="#e0ffff")

    def confirm(otp):
        try:
            if int(otp) == random_number:
                final(user_email)
            else:
                messagebox.showerror("Error", "Invalid OTP")
                print("err1")
        except:
            messagebox.showerror("Error", "Invalid OTP")
            print("err2")

    if index == 2 or index == 3 or index == 4:

        password = os.getenv("password")

        sender = os.getenv("sender")

        receiver = user_email
        random_number = random.randint(100000, 999999)
        print(random_number)


        message = "Your OTP for confirming order is " + str(random_number)
        subject = "Team TTE"

        email = "subject: {} \n\n {}".format(subject, message)

        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()

        s.login(sender, password)

        s.sendmail(sender, receiver, email)

        s.quit()
        Label(Pay_window, text="Enter OTP sent to your Email.", bg="#e0ffff", font=myFont2).grid(row=0, column=0,
                                                                                                 padx=5, pady=5)
        otp = Entry(Pay_window, font=myFont2)
        otp.grid(row=1, column=0, padx=5, pady=5, sticky=E + W)
        confirm_button = Button(Pay_window, text="Confirm", bg="green", fg="White", font=myFont3,
                                command=lambda: confirm(otp.get()))
        confirm_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=E + W)
    else:
        pass
    Pay_window.mainloop()


def checkout():
    global Checkout_Window, Checkout_Frame, first_name, last_name

    Restaurant_Open_Window.destroy()
    Checkout_Window = Tk()
    Checkout_Window.title("Checkout")
    Checkout_Window.config(bg="#e0ffff")

    email = info_dict["email"]

    first_name = ""
    last_name = ""

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    d = c.execute("select first_name, last_name, email from Customer_Info")
    d = d.fetchall()
    for i, j, k in d:
        if k == email:
            first_name = i
            last_name = j

    conn.commit()
    conn.close()

    Name_Frame = LabelFrame(Checkout_Window, text="Details", bg="#e0ffff", font=myFont2, padx=3, pady=3)
    Name_Frame.grid(row=1, column=0, padx=7, pady=7)
    Item_Frame = LabelFrame(Checkout_Window, text="Cart", bg="#e0ffff", font=myFont2, padx=3, pady=3)
    Item_Frame.grid(row=0, column=0, columnspan=2, padx=7, pady=7)
    Checkout_Frame = LabelFrame(Checkout_Window, text="Select payment method", bg="#e0ffff", font=myFont2, padx=3,
                                pady=3)
    Checkout_Frame.grid(row=1, column=1, padx=7, pady=7)

    Label(Name_Frame, text="Name: ").grid(row=0, column=0, sticky="w")
    Label(Name_Frame, text=first_name + last_name, bg="#e0ffff").grid(row=0, column=1, sticky=W)
    Label(Name_Frame, text="Email: ").grid(row=1, column=0, sticky="w")
    Label(Name_Frame, text=email, bg="#e0ffff").grid(row=1, column=1, sticky=W)
    Label(Name_Frame, text="Address: ").grid(row=2, column=0, sticky="w")
    Label(Name_Frame, text=info_dict["Address"], bg="#e0ffff").grid(row=2, column=1, sticky=W)
    Label(Name_Frame, text="City: ").grid(row=3, column=0, sticky="w")
    Label(Name_Frame, text=info_dict["City"], bg="#e0ffff").grid(row=3, column=1, sticky=W)
    Label(Name_Frame, text="Zipcode: ").grid(row=4, column=0, sticky="w")
    Label(Name_Frame, text=info_dict["Zipcode"], bg="#e0ffff").grid(row=4, column=1, sticky=W)

    row__topping_index = 5
    final_total_price = 0
    for name, quantity, price, topping in cart_list:
        Label(Item_Frame, text=name, bg="#e0ffff", font=myFont2).grid(row=row__topping_index, column=0, sticky=W)
        row__topping_index += 1
        topping = ",".join(topping)
        Label(Item_Frame, text=topping, bg="#e0ffff").grid(row=row__topping_index, column=0, sticky=W)
        row__topping_index += 1
        Label(Item_Frame, text=quantity, bg="#e0ffff").grid(row=row__topping_index, column=0, sticky=W)
        Label(Item_Frame, text=price, bg="#e0ffff").grid(row=row__topping_index, column=1, sticky=W)
        row__topping_index += 1
        tot_price = int(quantity) * int(price)
        final_total_price += tot_price
        tot_price = str(tot_price)
        row__topping_index += 1

    Label(Item_Frame, text="Total Price: " + str(final_total_price), bg="#e0ffff", font=myFont2).grid(
        row=row__topping_index, column=0, sticky=W + E)

    # Label(Checkout_Frame, text="Select payment method").grid(row=0, column=0)
    payment_mode = IntVar()
    Radiobutton(Checkout_Frame, text="Paytm", value=2, bg="#e0ffff", variable=payment_mode).grid(row=1, column=0,
                                                                                                 sticky=W)
    Radiobutton(Checkout_Frame, text="Google pay", value=3, bg="#e0ffff", variable=payment_mode).grid(row=2, column=0,
                                                                                                      sticky=W)
    Radiobutton(Checkout_Frame, text="Cash on delivery", bg="#e0ffff", value=4, variable=payment_mode).grid(row=3,
                                                                                                            column=0,
                                                                                                            sticky=W)
    Button(Checkout_Frame, text="Pay", bg="green", fg="white", command=lambda: pay(payment_mode.get(), email)).grid(
        row=4, column=0, sticky=W + E)

    checkout_row_index = 0

    Checkout_Window.mainloop()


def add_to_cart(name, qty, price, toppings=[]):
    topping_window.destroy()
    global row_index, cart_list, ttotal_price, checkout_button, total_price, Total_label, Total_price
    try:
        Total_label.destroy()
        Total_price.destroy()
        checkout_button.destroy()
    except:
        pass
    Label(Add_To_Cart_Frame, text="My Order", bg="green", fg="white", width=30).grid(row=0, column=0, columnspan=4)
    Label(Add_To_Cart_Frame, text="ITEM").grid(row=1, column=0)
    Label(Add_To_Cart_Frame, text="PRICE").grid(row=1, column=1)
    Label(Add_To_Cart_Frame, text="QTY").grid(row=1, column=2)
    Label(Add_To_Cart_Frame, text="TOTAL").grid(row=1, column=3)
    row_index += 2
    Label(Add_To_Cart_Frame, text=name).grid(row=row_index, column=0)
    Label(Add_To_Cart_Frame, text=price).grid(row=row_index, column=1)
    Label(Add_To_Cart_Frame, text=qty).grid(row=row_index, column=2)
    # row_index += 1
    ttotal_price = int(qty) * int(price)
    Label(Add_To_Cart_Frame, text=ttotal_price).grid(row=row_index, column=3)
    total_price += ttotal_price
    row_index += 1
    Total_label = Label(Add_To_Cart_Frame, text="TOTAL")
    Total_label.grid(row=row_index, column=2)
    Total_price = Label(Add_To_Cart_Frame, text=total_price)
    Total_price.grid(row=row_index, column=3)
    row_index += 2
    checkout_button = Button(Add_To_Cart_Frame, text="Checkout", command=checkout, bg="yellow", relief="ridge")
    checkout_button.grid(row=row_index, column=0)
    topping = []
    for j, k in toppings:
        if j != 0:
            topping.append(k)
            pass
    pdt = [name, qty, price, topping]
    cart_list.append(pdt)


def info(info_dic):
    global info_dict
    info_dict = info_dic


def quantity():
    quantity = [1, 2, 3, 4, 5]
    quantity_dropdown = ttk.Combobox(topping_window, value=quantity, text="Select Quantity")
    quantity_dropdown.current(0)
    return quantity_dropdown


def topping(restaurant_index, food_index):
    global topping_window, restaurant_index_1, Font_tuple
    Font_tuple = ("Arial", 14)
    restaurant_index_1 = restaurant_index
    topping_window = Toplevel(Restaurant_Open_Window)
    topping_window.config(bg="#e0ffff")

    if restaurant_index == 0:
        food_image = Image.open(BalanDosa_Image_List[food_index])
        food_image = food_image.resize((200, 200), Image.ANTIALIAS)
        food_image1 = ImageTk.PhotoImage(food_image)
        a = Label(topping_window, image=food_image1)
        a.grid(row=0, column=0)
        name = BalanDosa_Name_List[food_index]
        price = BalanDosa_Price_List[food_index]
        bdn = Label(topping_window, text=name, fg="Green", bg="yellow")
        bdn.grid(row=0, column=1, padx=10, pady=20, sticky='w')
        bdn.config(font=Font_tuple)
        bdq = Label(topping_window, text="Select Quantity", bg="green", fg="White", anchor="w", width=15)
        bdq.grid(row=1, column=0, padx=10, pady=20, sticky='w')
        bdq.config(font=Font_tuple)
        quantity_dropdown = quantity()
        quantity_dropdown.grid(row=1, column=1, pady=20)
        Button(topping_window, text="Add to Cart",
               command=lambda: add_to_cart(name, quantity_dropdown.get(), price)).grid(row=2, column=0)
    elif restaurant_index == 1:
        food_image = Image.open(ChocolateRoom_Image_List[food_index])
        food_image = food_image.resize((200, 200), Image.ANTIALIAS)
        food_image1 = ImageTk.PhotoImage(food_image)
        a = Label(topping_window, image=food_image1)
        a.grid(row=0, column=0)
        name = ChocolateRoom_Name_List[food_index]
        price = ChocolateRoom_Price_List[food_index]
        Label(topping_window, text=name, font=myFont1, fg="Green", bg="yellow").grid(row=0, column=1, padx=10, pady=20,
                                                                                     sticky='w')
        Label(topping_window, text="Select Quantity", font=myFont1, bg="green", fg="White", anchor="w", width=15).grid(
            row=1, column=0, padx=10, pady=20, sticky='w')
        quantity_dropdown = quantity()
        quantity_dropdown.grid(row=1, column=1)
        Button(topping_window, text="Add to Cart", font=myFont1, bg="green", fg="White",
               command=lambda: add_to_cart(name, quantity_dropdown.get(), price)).grid(row=2, column=0)
    elif restaurant_index == 2:
        food_image = Image.open(Dominos_Image_List[food_index])
        food_image = food_image.resize((200, 200), Image.ANTIALIAS)
        food_image1 = ImageTk.PhotoImage(food_image)
        a = Label(topping_window, image=food_image1)
        a.grid(row=0, column=0)
        name = Dominos_Name_List[food_index]
        price = Dominos_Price_List[food_index]
        Label(topping_window, text=name, font=myFont1, fg="Green", bg="yellow").grid(row=0, column=1, padx=10, pady=20,
                                                                                     sticky='w')
        Label(topping_window, text="Select toppings", font=myFont1, bg="green", fg="White", anchor="w", width=15).grid(
            row=1, column=0, padx=10, pady=20, sticky='w')
        c1 = IntVar()
        Checkbutton(topping_window, text="Cheese dip", bg="#e0ffff", variable=c1).grid(row=2, column=0)
        c2 = IntVar()
        Checkbutton(topping_window, text="Peri Peri dip", bg="#e0ffff", variable=c2).grid(row=3, column=0)
        Label(topping_window, text="Select Quantity", font=myFont1, bg="green", fg="White", anchor="w", width=15).grid(
            row=4, column=0, padx=10, pady=20, sticky='w')
        quantity_dropdown = quantity()
        quantity_dropdown.grid(row=4, column=1)
        Button(topping_window, text="Add to Cart", font=myFont1, bg="green", fg="White",
               command=lambda: add_to_cart(name, quantity_dropdown.get(), price,
                                           [(c1.get(), "Cheese Dip"), (c2.get(), "Peri Peri dip")])).grid(row=5,
                                                                                                          column=0)
    elif restaurant_index == 3:
        food_image = Image.open(JassiDaParatha_Image_List[food_index])
        food_image = food_image.resize((200, 200), Image.ANTIALIAS)
        food_image1 = ImageTk.PhotoImage(food_image)
        a = Label(topping_window, image=food_image1)
        a.grid(row=0, column=0)
        name = JassiDaParatha_Name_List[food_index]
        price = JassiDaParatha_Price_List[food_index]
        Label(topping_window, text=name, font=myFont1, fg="Green", bg="yellow").grid(row=0, column=1, padx=10, pady=20,
                                                                                     sticky='w')
        Label(topping_window, text="Select Quantity", font=myFont1, bg="green", fg="White", anchor="w", width=15).grid(
            row=1, column=0, padx=10, pady=20, sticky='w')
        quantity_dropdown = quantity()
        quantity_dropdown.grid(row=1, column=1)
        Button(topping_window, text="Add to Cart", font=myFont1, bg="green", fg="White",
               command=lambda: add_to_cart(name, quantity_dropdown.get(), price)).grid(row=2, column=0)
    elif restaurant_index == 4:
        food_image = Image.open(Lapinos_Image_List[food_index])
        food_image = food_image.resize((200, 200), Image.ANTIALIAS)
        food_image1 = ImageTk.PhotoImage(food_image)
        a = Label(topping_window, image=food_image1)
        a.grid(row=0, column=0)
        name = Lapinos_Name_List[food_index]
        price = Lapinos_Price_List[food_index]
        Label(topping_window, text=name, font=myFont1, fg="Green", bg="yellow").grid(row=0, column=1, padx=10, pady=20,
                                                                                     sticky='w')
        Label(topping_window, text="Select toppings", font=myFont1, bg="green", fg="White", anchor="w", width=15).grid(
            row=1, column=0, padx=10, pady=20, sticky='w')
        c1 = IntVar()
        Checkbutton(topping_window, text="Cheesy Dip", bg="#e0ffff", variable=c1).grid(row=2, column=0)
        c2 = IntVar()
        Checkbutton(topping_window, text="Peri Peri Dip", bg="#e0ffff", variable=c2).grid(row=3, column=0)
        c3 = IntVar()
        Checkbutton(topping_window, text="Garlic Dip", bg="#e0ffff", variable=c3).grid(row=4, column=0)
        c4 = IntVar()
        Checkbutton(topping_window, text="Jalapenos", bg="#e0ffff", variable=c4).grid(row=5, column=0)
        c5 = IntVar()
        Checkbutton(topping_window, text="Mushroom", bg="#e0ffff", variable=c5).grid(row=6, column=0)
        c6 = IntVar()
        Checkbutton(topping_window, text="Red Peprika", bg="#e0ffff", variable=c6).grid(row=7, column=0)

        Label(topping_window, text="Select Quantity", font=myFont1, bg="green", fg="White", anchor="w", width=15).grid(
            row=8, column=0, padx=10, pady=20, sticky='w')
        quantity_dropdown = quantity()
        quantity_dropdown.grid(row=8, column=1)
        Button(topping_window, text="Add to Cart", font=myFont1, bg="green", fg="White",
               command=lambda: add_to_cart(name, quantity_dropdown.get(), price,
                                           [(c1.get(), "Cheesy Dip"), (c2.get(), "Peri Peri Dip"),
                                            (c3.get(), "Garlic Dip"), (c4.get(), "Jalapenos"), (c5.get(), "Mushroom"),
                                            (c6.get(), "Red Peprika")])).grid(row=9, column=0)
    elif restaurant_index == 5:
        food_image = Image.open(McDonalds_Image_List[food_index])
        food_image = food_image.resize((200, 200), Image.ANTIALIAS)
        food_image1 = ImageTk.PhotoImage(food_image)
        a = Label(topping_window, image=food_image1)
        a.grid(row=0, column=0)
        name = McDonalds_Name_List[food_index]
        price = McDonalds_Price_List[food_index]
        Label(topping_window, text=name, font=myFont1, fg="Green", bg="yellow").grid(row=0, column=1, padx=10, pady=20,
                                                                                     sticky='w')
        Label(topping_window, text="Select Quantity", font=myFont1, bg="green", fg="White", anchor="w", width=15).grid(
            row=1, column=0, padx=10, pady=20, sticky='w')
        quantity_dropdown = quantity()
        quantity_dropdown.grid(row=1, column=1)
        Button(topping_window, text="Add to Cart", font=myFont1, bg="green", fg="White",
               command=lambda: add_to_cart(name, quantity_dropdown.get(), price)).grid(row=2, column=0)
    elif restaurant_index == 6:
        food_image = Image.open(Subway_Image_List[food_index])
        food_image = food_image.resize((200, 200), Image.ANTIALIAS)
        food_image1 = ImageTk.PhotoImage(food_image)
        a = Label(topping_window, image=food_image1)
        a.grid(row=0, column=0)
        name = Subway_Name_List[food_index]
        price = Subway_Price_List[food_index]
        Label(topping_window, text=name, font=myFont1, fg="Green", bg="yellow").grid(row=0, column=1, padx=10, pady=20,
                                                                                     sticky='w')
        Label(topping_window, text="Select Bread", font=myFont1, bg="green", fg="White", anchor="w", width=15).grid(
            row=1, column=0, padx=10, pady=20, sticky='w')

        c = IntVar()
        Radiobutton(topping_window, text="Flat Bread", bg="#e0ffff", variable=c, value=1).grid(row=2, column=0, sticky="w", padx=30)
        Radiobutton(topping_window, text="Multigrain Bread", bg="#e0ffff", variable=c, value=2).grid(row=3, column=0, sticky="w", padx=30)
        Radiobutton(topping_window, text="Roasted Garlic Bread", bg="#e0ffff", variable=c, value=3).grid(row=4,
                                                                                                         column=0, sticky="w", padx=30)
        Radiobutton(topping_window, text="Parmesan Oregano Bread", bg="#e0ffff", variable=c, value=4).grid(row=5,
                                                                                                           column=0, sticky="w", padx=30)
        Radiobutton(topping_window, text="White Italian Bread", bg="#e0ffff", variable=c, value=5).grid(row=6, column=0, sticky="w", padx=30)

        Label(topping_window, text="Select toppings", font=myFont1, bg="green", fg="White", anchor="w", width=15).grid(
            row=1, column=1, padx=10, pady=20, sticky='w')
        c1 = IntVar()
        Checkbutton(topping_window, text="Lettuce", bg="#e0ffff", variable=c1).grid(row=2, column=1, sticky="w", padx=30)
        c2 = IntVar()
        Checkbutton(topping_window, text="Tomato", bg="#e0ffff", variable=c2).grid(row=3, column=1, sticky="w", padx=30)
        c3 = IntVar()
        Checkbutton(topping_window, text="Cucumbers", bg="#e0ffff", variable=c3).grid(row=4, column=1, sticky="w", padx=30)
        c4 = IntVar()
        Checkbutton(topping_window, text="Jalapenos", bg="#e0ffff", variable=c4).grid(row=5, column=1, sticky="w", padx=30)
        c5 = IntVar()
        Checkbutton(topping_window, text="Mushroom", bg="#e0ffff", variable=c5).grid(row=6, column=1, sticky="w", padx=30)
        c6 = IntVar()
        Checkbutton(topping_window, text="Onion", bg="#e0ffff", variable=c6).grid(row=7, column=1, sticky="w", padx=30)
        c7 = IntVar()
        Checkbutton(topping_window, text="Olives", bg="#e0ffff", variable=c7).grid(row=8, column=1, sticky="w", padx=30)
        c8 = IntVar()
        Checkbutton(topping_window, text="Pickle", bg="#e0ffff", variable=c8).grid(row=9, column=1, sticky="w", padx=30)
        c9 = IntVar()
        Checkbutton(topping_window, text="Capsicums", bg="#e0ffff", variable=c9).grid(row=10, column=1, sticky="w", padx=30)

        Label(topping_window, text="Select Sauce", font=myFont1, bg="green", fg="White", anchor="w", width=15).grid(
            row=1, column=2, padx=10, pady=20, sticky='w')
        c11 = IntVar()
        Checkbutton(topping_window, text="Mayonnaice Sauce", bg="#e0ffff", variable=c11).grid(row=2, column=2, sticky="w", padx=30)
        c22 = IntVar()
        Checkbutton(topping_window, text="Mint Mayonnaice Sauce", bg="#e0ffff", variable=c22).grid(row=3, column=2, sticky="w", padx=30)
        c33 = IntVar()
        Checkbutton(topping_window, text="Honey Mustard Sauce", bg="#e0ffff", variable=c33).grid(row=4, column=2, sticky="w", padx=30)
        c44 = IntVar()
        Checkbutton(topping_window, text="Tandoori Mayo Sauce", bg="#e0ffff", variable=c44).grid(row=5, column=2, sticky="w", padx=30)
        c55 = IntVar()
        Checkbutton(topping_window, text="Sweet Onion Sauce", bg="#e0ffff", variable=c55).grid(row=6, column=2, sticky="w", padx=30)
        c66 = IntVar()
        Checkbutton(topping_window, text="Barbeque Sauce", bg="#e0ffff", variable=c66).grid(row=7, column=2, sticky="w", padx=30)
        c77 = IntVar()
        Checkbutton(topping_window, text="Marinara Sauce", bg="#e0ffff", variable=c77).grid(row=8, column=2, sticky="w", padx=30)
        c88 = IntVar()
        Checkbutton(topping_window, text="South West Sauce", bg="#e0ffff", variable=c88).grid(row=9, column=2, sticky="w", padx=30)
        c99 = IntVar()
        Checkbutton(topping_window, text="Red Chilli Sauce", bg="#e0ffff", variable=c99).grid(row=10, column=2, sticky="w", padx=30)

        temp = ["Flat Bread", "Multigrain Bread", "Roasted Garlic Bread", "Parmesan Oregano Bread",
                "White Italian Bread"]
        Label(topping_window, text="Select Quantity", font=myFont1, bg="green", fg="White", anchor="w", width=15).grid(
            row=11, column=0, padx=10, pady=20, sticky='w')
        quantity_dropdown = quantity()
        quantity_dropdown.grid(row=11, column=1)
        Button(topping_window, text="Add to Cart", font=myFont1, bg="green", fg="White",
               command=lambda: add_to_cart(name, quantity_dropdown.get(), price,
                                           [(c.get(), temp[c.get() - 1]), (c11.get(), "Mayonnaice Sauce"),
                                            (c22.get(), "Mint Mayonnaice Sauce"), (c33.get(), "Honey Mustard Sauce"),
                                            (c44.get(), "Tandoori Mayo Sauce"), (c55.get(), "Sweet Onion Sauce"),
                                            (c66.get(), "Barbeque Sauce"), (c77.get(), "Marinara Sauce"),
                                            (c88.get(), "South West Sauce"), (c99.get(), "Red Chilli Sauce"),
                                            (c1.get(), "Lettuce"), (c2.get(), "Tomato"), (c3.get(), "Cucumbers"),
                                            (c4.get(), "Jalapenos"), (c5.get(), "Mushroom"), (c6.get(), "Onion"),
                                            (c7.get(), "Olives"), (c8.get(), "Pickle"), (c9.get(), "Capsicums")])).grid(
            row=12, column=0)
    topping_window.mainloop()


def intermediate():
    Restaurant_Open_Window.destroy()
    global cart_list, total_price
    cart_list = []
    total_price = 0
    application()


def food_grid(frame1, list1, name, price, restaurant_index):
    col = 0
    row = 1
    flag = 0
    for i, j in list1:  # Gridding food items in frame
        j.grid(row=row, column=col,ipadx=20)
        if flag < 3:
            col += 1
            flag += 1
        else:
            flag = 0
            col = 0
            row += 3

    col = 0
    row = 2
    flag = 0
    for i in name:  # Gridding food Name in frame
        Label(frame1, bg="#e0ffff", padx=2, pady=2, text=i).grid(row=row, column=col, padx=2, pady=2)
        if flag < 3:
            col += 1
            flag += 1
        else:
            flag = 0
            col = 0
            row += 3

    col = 0
    row = 3
    flag = 0
    for i in price:  # Gridding food price in frame as button
        Button(frame1, text=i,bg="#FAEBD7",padx=10,
               command=lambda x=restaurant_index, y=price.index(i): topping(x, y)).grid(row=row,
                                                                                        column=col,
                                                                                        padx=2, pady=2)
        if flag < 3:
            col += 1
            flag += 1
        else:
            flag = 0
            col = 0
            row += 3

    back = Button(Restaurant_Open_Window, text="Back", font=myFont2, command=intermediate, bg="green", fg="white",
                  relief="ridge", width=10).grid(row=row + 1, column=0, pady=5)


def func(restaurant_index):
    application_window.destroy()
    global Restaurant_Open_Window, Restaurant_Open_Frame, Add_To_Cart_Frame, myFont1
    Restaurant_Open_Window = Tk()
    Restaurant_Open_Window.config(bg="#e0ffff")

    Restaurant_Open_Frame = LabelFrame(Restaurant_Open_Window, bg="#e0ffff", padx=10, borderwidth=0,
                                       highlightthickness=0)
    Restaurant_Open_Frame.grid(row=1, column=0, sticky=W)
    Add_To_Cart_Frame = LabelFrame(Restaurant_Open_Window, bg="#e0ffff", borderwidth=0, highlightthickness=0)
    Add_To_Cart_Frame.grid(row=1, column=1, padx=7, pady=7)
    temp_frame = LabelFrame(Restaurant_Open_Window, bg="#e0ffff", borderwidth=0, highlightthickness=0)
    temp_frame.grid(row=0, column=0, columnspan=2)

    if restaurant_index == 0:
        temp = Image.open("GUI/Restaurants/balandosabg.png")
        temp = temp.resize((507, 110), Image.ANTIALIAS)
        temp = ImageTk.PhotoImage(temp)

        menu = Label(Restaurant_Open_Frame, text="Explore Menu", font=myFont1, bg="green", fg="White", anchor="w",
                     width=30)
        menu.grid(row=0, column=0, columnspan=4, padx=3, pady=3, sticky='w')

        Label(temp_frame, image=temp).grid(row=0, column=0)

        image_resize_call(BalanDosa_Image_List, BalanDosa_Image_List1, Restaurant_Open_Frame, 0)
        food_grid(Restaurant_Open_Frame, BalanDosa_Image_List1, BalanDosa_Name_List, BalanDosa_Price_List,
                  restaurant_index)
    elif restaurant_index == 1:
        temp = Image.open("GUI/Restaurants/chocolatebg.png")
        temp = temp.resize((507, 110), Image.ANTIALIAS)
        temp = ImageTk.PhotoImage(temp)
        temp_frame = LabelFrame(Restaurant_Open_Window, borderwidth=0, highlightthickness=0)
        temp_frame.grid(row=0, column=0, columnspan=2)

        menu = Label(Restaurant_Open_Frame, text="Explore Menu", font=myFont1, bg="green", fg="White", anchor="w",
                     width=30)
        menu.grid(row=0, column=0, columnspan=4, padx=3, pady=3, sticky='w')

        Label(temp_frame, image=temp).grid(row=0, column=0)

        image_resize_call(ChocolateRoom_Image_List, ChocolateRoom_Image_List1, Restaurant_Open_Frame, 0)
        food_grid(Restaurant_Open_Frame, ChocolateRoom_Image_List1, ChocolateRoom_Name_List, ChocolateRoom_Price_List,
                  restaurant_index)
    elif restaurant_index == 2:
        temp = Image.open("GUI/Restaurants/Dominozbg.png")
        temp = temp.resize((657, 90), Image.ANTIALIAS)
        temp = ImageTk.PhotoImage(temp)
        temp_frame = LabelFrame(Restaurant_Open_Window, borderwidth=0, highlightthickness=0)
        temp_frame.grid(row=0, column=0, columnspan=2)

        menu = Label(Restaurant_Open_Frame, text="Explore Menu", font=myFont1, bg="green", fg="White", anchor="w",
                     width=30)
        menu.grid(row=0, column=0, columnspan=4,padx=10,pady=20,sticky='w')

        Label(temp_frame, image=temp).grid(row=0, column=0)

        image_resize_call(Dominos_Image_List, Dominos_Image_List1, Restaurant_Open_Frame, 0)
        food_grid(Restaurant_Open_Frame, Dominos_Image_List1, Dominos_Name_List, Dominos_Price_List, restaurant_index)
    elif restaurant_index == 3:
        temp = Image.open("GUI/Restaurants/jassidaparathabg.jpg")
        temp = temp.resize((600, 200), Image.ANTIALIAS)
        temp = ImageTk.PhotoImage(temp)
        temp_frame = LabelFrame(Restaurant_Open_Window, borderwidth=0, highlightthickness=0)
        temp_frame.grid(row=0, column=0, columnspan=2)

        menu = Label(Restaurant_Open_Frame, text="Explore Menu", font=myFont1, bg="green", fg="White", anchor="w",
                     width=35)
        menu.grid(row=0, column=0, columnspan=4, padx=3, pady=3, sticky='w')

        Label(temp_frame, image=temp).grid(row=0, column=0)

        image_resize_call(JassiDaParatha_Image_List, JassiDaParatha_Image_List1, Restaurant_Open_Frame, 0)
        food_grid(Restaurant_Open_Frame, JassiDaParatha_Image_List1, JassiDaParatha_Name_List,
                  JassiDaParatha_Price_List, restaurant_index)
    elif restaurant_index == 4:
        temp = Image.open("GUI/Restaurants/lapinozbg.png")
        temp = temp.resize((507, 110), Image.ANTIALIAS)
        temp = ImageTk.PhotoImage(temp)
        temp_frame = LabelFrame(Restaurant_Open_Window, borderwidth=0, highlightthickness=0)
        temp_frame.grid(row=0, column=0, columnspan=2)

        menu = Label(Restaurant_Open_Frame, text="Explore Menu", font=myFont1, bg="green", fg="White", anchor="w",
                     width=35)
        menu.grid(row=0, column=0, columnspan=4, padx=3, pady=3, sticky='w')

        Label(temp_frame, image=temp).grid(row=0, column=0)

        image_resize_call(Lapinos_Image_List, Lapinos_Image_List1, Restaurant_Open_Frame, 0)
        food_grid(Restaurant_Open_Frame, Lapinos_Image_List1, Lapinos_Name_List, Lapinos_Price_List, restaurant_index)
    elif restaurant_index == 5:
        temp = Image.open("GUI/Restaurants/mcdonaldsbg.jpeg")
        temp = temp.resize((600, 200), Image.ANTIALIAS)
        temp = ImageTk.PhotoImage(temp)
        temp_frame = LabelFrame(Restaurant_Open_Window, borderwidth=0, highlightthickness=0)
        temp_frame.grid(row=0, column=0, columnspan=2)

        menu = Label(Restaurant_Open_Frame, text="Explore Menu", font=myFont1, bg="green", fg="White", anchor="w",
                     width=35)
        menu.grid(row=0, column=0, columnspan=4, padx=3, pady=3, sticky='w')

        Label(temp_frame, image=temp).grid(row=0, column=0)

        image_resize_call(McDonalds_Image_List, McDonalds_Image_List1, Restaurant_Open_Frame, 0)
        food_grid(Restaurant_Open_Frame, McDonalds_Image_List1, McDonalds_Name_List, McDonalds_Price_List,
                  restaurant_index)
    elif restaurant_index == 6:
        temp = Image.open("GUI/Restaurants/subwaybg.png")
        temp = temp.resize((507, 110), Image.ANTIALIAS)
        temp = ImageTk.PhotoImage(temp)
        temp_frame = LabelFrame(Restaurant_Open_Window, borderwidth=0, highlightthickness=0)
        temp_frame.grid(row=0, column=0, columnspan=2)

        menu = Label(Restaurant_Open_Frame, text="Explore Menu", font=myFont1, bg="green", fg="White", anchor="w",
                     width=35)
        menu.grid(row=0, column=0, columnspan=4, padx=3, pady=3, sticky='w')

        Label(temp_frame, image=temp).grid(row=0, column=0)

        image_resize_call(Subway_Image_List, Subway_Image_List1, Restaurant_Open_Frame, 0)
        food_grid(Restaurant_Open_Frame, Subway_Image_List1, Subway_Name_List, Subway_Price_List, restaurant_index)

    Restaurant_Open_Window.mainloop()


def image_resize(img, frame, i, flag):
    if flag == 2:
        img = Image.open(img)
        img = img.resize((40, 20), Image.ANTIALIAS)
        myimage = ImageTk.PhotoImage(img)
        button = Label(frame, image=myimage)
    else:
        img = Image.open(img)
        img = img.resize((100, 100), Image.ANTIALIAS)
        myimage = ImageTk.PhotoImage(img)
        if flag == 1:
            button = Button(frame, text="abc", image=myimage, command=lambda x=i: func(x))
        else:
            button = Label(frame, image=myimage)

    return myimage, button


def image_resize_call(List, List1, frame, flag):
    for i in List:
        List1.append(image_resize(i, frame, List.index(i), flag))


def restaurant_grid(List1, List2):
    row = 0
    col = 0
    for i, j in List1:
        j.grid(row=row, column=col, padx=10)
        if col < 2:
            col += 1
        else:
            col = 0
            row += 2
    row = 1
    col = 0
    flag = 0
    for i, j in List2:
        j.grid(row=row, column=col)
        if col < 2:
            col += 1
        else:
            col = 0
            row += 2
    # k = 0
    # for i, j in List1:
    #     if k % 3 == 0:
    #         j.grid(row=int((k / 3)), column=0)
    #         k += 1
    #     elif k % 3 == 1:
    #         j.grid(row=int((k / 3)), column=1)
    #         k += 1
    #     elif k % 3 == 2:
    #         j.grid(row=int((k / 3)), column=2)
    #         k += 1


def application():
    global Restaurant_Name_List, myFont2, myFont3, myFont1, myFont, Subway_Price_List, Subway_Name_List, McDonalds_Price_List, McDonalds_Name_List, Lapinos_Price_List, Lapinos_Name_List, JassiDaParatha_Price_List, JassiDaParatha_Name_List, JassiDaParatha_Image_List1, JassiDaParatha_Image_List, ChocolateRoom_Price_List, ChocolateRoom_Name_List, application_window, Restaurant, Restaurant_Image_List, Restaurant_Image_List1, BalanDosa_Image_List, BalanDosa_Image_List1, BalanDosa_Name_List, BalanDosa_Price_List, ChocolateRoom_Image_List, ChocolateRoom_Image_List1, Dominos_Image_List, Dominos_Image_List1, Dominos_Name_List, Dominos_Price_List, Lapinos_Image_List, Lapinos_Image_List1, McDonalds_Image_List, McDonalds_Image_List1, Subway_Image_List, Subway_Image_List1
    application_window = Tk()
    application_window.title("Application")
    application_window.config(bg="#ffe8f0")

    myFont = font.Font(size=20)
    myFont1 = font.Font(size=15)
    myFont2 = font.Font(size=13)
    myFont3 = font.Font(size=6)

    bg = Image.open("Images/delivery.png")
    bg = bg.resize((320, 500), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(bg)
    bg_frame = LabelFrame(application_window, borderwidth=0, highlightthickness=0)
    bg_frame.grid(row=0, column=0)
    Label(bg_frame, image=bg).grid(row=0, column=0)

    Restaurant = LabelFrame(application_window, padx=7, pady=7, bg="#ffe8f0", text="Restaurants", font=myFont2)
    Restaurant.grid(row=0, column=1, padx=7, pady=10)

    rating_list = ["Rating/r1.png", "Rating/r5.png", "Rating/r4.png", "Rating/r3.png", "Rating/r1.png", "Rating/r2.png",
                   "Rating/r3.png"]
    rating_list1 = []
    image_resize_call(rating_list, rating_list1, Restaurant, 2)

    Restaurant_Name_List = ["Balan Dosa", "Chocolate Room 380060", "Dominos Pizza 380060", "Jassi da paratha",
                            "Lapinoz pizza 380060", "Mc. Donalds 380060", "Subway 380060"]

    Restaurant_Image_List = ["Gui/BalanDosa/BalanDosa.jpeg", "Gui/Chocolate Room/chocolateroom.jpeg",
                             "Gui/Dominos/dominose logo.jpg", "Gui/Jassi da paratha/Jassi da paratha.jpg",
                             "Gui/lapinoz/lapinoze logo.jpg", "Gui/mcdonalds/Macdonalds logo.png",
                             "Gui/subway/Subway logo.jpg"]
    Restaurant_Image_List1 = []
    image_resize_call(Restaurant_Image_List, Restaurant_Image_List1, Restaurant, 1)
    restaurant_grid(Restaurant_Image_List1, rating_list1)

    BalanDosa_Image_List = ["Gui/BalanDosa/CheseUtappam.jpeg", "Gui/BalanDosa/ChessMysore.jpeg",
                            "Gui/BalanDosa/masalaDosa.jpeg", "Gui/BalanDosa/MysoreMasalaDosa.jpeg",
                            "Gui/BalanDosa/Paneerdosa.jpeg", "Gui/BalanDosa/paperDosa.jpeg",
                            "Gui/BalanDosa/RavaUttapam.jpeg", "Gui/BalanDosa/SchezwanDosa.jpeg",
                            "Gui/BalanDosa/springRoll.jpeg", "Gui/BalanDosa/TajMahelDosa.jpeg"]
    BalanDosa_Image_List1 = []
    BalanDosa_Name_List = ["Cheese Utappam", "Chess Mysore", "Masala Dosa", "Mysore Masala Dosa", "Paneer Dosa",
                           "Paper Dosa", "Rava Uttapam", "Schezwan Dosa", "Spring Roll", "Taj Mahel Dosa"]
    BalanDosa_Price_List = [140, 130, 120, 144, 160, 110, 165, 170, 145, 220]

    ChocolateRoom_Image_List = ["Gui/Chocolate Room/BrownieSundae.jpg", "Gui/Chocolate Room/Cappucinno.jpg",
                                "Gui/Chocolate Room/Chocalatecake.jpeg", "Gui/Chocolate Room/ChocolateSizzler.jpeg",
                                "Gui/Chocolate Room/DarkHotchoco.jpeg", "Gui/Chocolate Room/ecstasySundae.jpg",
                                "Gui/Chocolate Room/lemonicetea.jpeg", "Gui/Chocolate Room/minihearcake.jpeg",
                                "Gui/Chocolate Room/NutellaCoffe.jpg", "Gui/Chocolate Room/TruffleCake.jpeg"]
    ChocolateRoom_Image_List1 = []
    ChocolateRoom_Name_List = ["Brownie Sundae", "Cappucinno", "Chocalate Cake", "Chocolate Sizzler", "Dark Hot Choco",
                               "Ecstasy Sundae", "Lemonice Tea", "Mini Heart Cake", "Nutella Coffee", "Truffle Cake"]
    ChocolateRoom_Price_List = [180, 150, 540, 170, 159, 730, 155, 190, 120, 510]

    Dominos_Image_List = ["Gui/Dominos/choco lake.jpg", "Gui/Dominos/Farmhouse.jpg",
                          "Gui/Dominos/garlic breadsticks.jfif", "Gui/Dominos/golden_corn_veg.jpg",
                          "Gui/Dominos/margharita dominose.jfif", "Gui/Dominos/Mexican_Green_Wave.jpg",
                          "Gui/Dominos/new_cheese_n_corn.jpg", "Gui/Dominos/stuffed-garlic-breadstick.jpg",
                          "Gui/Dominos/Veggie_Paradise.jpg", "Gui/Dominos/VegLoadedL.jpg"]
    Dominos_Image_List1 = []
    Dominos_Name_List = ["Choco Lava Cake", "Farmhouse", "Garlic Breadsticks", "Golden Corn Veg", "Margharita",
                         "Mexican Green Wave", "Cheese n Corn", "Stuffed Garlic Breadstick", "Veggie Paradise",
                         "Veg Loaded"]
    Dominos_Price_List = [170, 235, 139, 185, 100, 245, 180, 160, 230, 185]

    JassiDaParatha_Image_List = ["Gui/Jassi da paratha/Dal Makhni.jfif", "Gui/Jassi da paratha/parathajfif.jfif",
                                 "Gui/Jassi da paratha/patiala-paneer.jpg",
                                 "Gui/Jassi da paratha/Tandoori-Paneer-Tikka-.jpg",
                                 "Gui/Jassi da paratha/Veg-Biryani.jpg"]
    JassiDaParatha_Image_List1 = []
    JassiDaParatha_Name_List = ["Dal Makhni", "Paratha", "Patiala Paneer", "Tandoori Paneer Tikka", "Veg Biryani"]
    JassiDaParatha_Price_List = [290, 200, 270, 295, 380]

    Lapinos_Image_List = ["Gui/lapinoz/Cheesy 7.jpg", "Gui/lapinoz/Choco Lava Cake.jpg",
                          "Gui/lapinoz/English Retreat Pizza.jpg", "Gui/lapinoz/Farm Villa.jpg",
                          "Gui/lapinoz/Garlic Bread.jpg", "Gui/lapinoz/Italian Pastajpg.jpg",
                          "Gui/lapinoz/Margharita Pizza.jpg", "Gui/lapinoz/Peri_Peri_Paneer_Pizza.jpg",
                          "Gui/lapinoz/Stuffed Garlic Bread.jfif", "Gui/lapinoz/Veg Americano Pasta.jpg"]
    Lapinos_Image_List1 = []
    Lapinos_Name_List = ["Cheesy 7", "Choco Lava Cake", "English Retreat Pizza", "Farm Villa", "Garlic Bread",
                         "Italian Pasta", "Margharita Pizza", "Peri Peri Paneer Pizza", "Stuffed Garlic Bread",
                         "Veg Americano Pasta"]
    Lapinos_Price_List = [170, 150, 210, 195, 80, 140, 115, 215, 90, 160]

    McDonalds_Image_List = ["Gui/mcdonalds/american-cheese-supreme-chicken.png",
                            "Gui/mcdonalds/chicken maharaja mac.jfif", "Gui/mcdonalds/mac maharaja mac.jfif",
                            "Gui/mcdonalds/mc chicken.jpg", "Gui/mcdonalds/McAloo-tikki.jpg",
                            "Gui/mcdonalds/mcveggie.jpg", "Gui/mcdonalds/Mexican McAloo Tikki Burger.jpg"]
    McDonalds_Image_List1 = []
    McDonalds_Name_List = ["American Cheese Supreme Chicken", "Chicken Maharaja Mac", "Mac Maharaja Mac", "Mc. Chicken",
                           "Mc. Aloo Tikki", "Mc. Veggie", "Mexican Mc. Aloo Tikki"]
    McDonalds_Price_List = [120, 135, 129, 124, 49, 109, 104]

    Subway_Image_List = ["Gui/subway/Chicken Kofta.jpg", "Gui/subway/Chicken Strips Salad.jfif",
                         "Gui/subway/corn-and-peas-sandwich-5.jpg", "Gui/subway/Hara Bhara Kabab.jfif",
                         "Gui/subway/Mexican PAtty.jpg", "Gui/subway/PaneerTikka.jpg", "Gui/subway/Subway Salad.jpg",
                         "Gui/subway/Subway-Veggie-Delite-Salad.jpg", "Gui/subway/Tandoori_Tofu_Sub.jpg",
                         "Gui/subway/veggie delite.jfif"]
    Subway_Image_List1 = []
    Subway_Name_List = ["Chicken Kofta", "Chicken Strips Salad", "Corn n Peas Sandwich", "Hara Bhara Kabab",
                        "Mexican Patty", "Paneer Tikka", "Subway Salad", "Subway Veggie Delite Salad",
                        "Tandoori Tofu Sub", "Veggie Delite"]
    Subway_Price_List = [140, 205, 185, 180, 177, 235, 230, 265, 245, 173]

    application_window.mainloop()

# info({'email': 'vrukshaldpatel274@gmail.com', 'City': 'Ahmedabad', 'Address': 'harivila apartment\n', 'Zipcode': '380061'})
# application()
