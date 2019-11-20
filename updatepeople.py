from tkinter import *
import sqlite3
from tkinter import messagebox
con = sqlite3.connect('database.db')
cur = con.cursor()


class Update(Toplevel):
    def __init__(self, person_id):
        Toplevel. __init__(self)

        self.geometry("650x650+600+200")
        self.iconbitmap(r"icons.ico")
        self.title("Update Person")
        self.resizable(False,False)
        print("person_id =", person_id)
        query = "select * from addressbook where person_id = '{}'".format(person_id)
        result = cur.execute(query).fetchone()
        print(result)
        self.person_id = person_id
        person_name = result[1]
        person_surname = result[2]
        person_email = result[3]
        person_phone = result[4]
        person_address = result[5]
        print("person name", person_name)

        self.top = Frame(self, height=150, bg='#2378e8')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#9923e8")
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file="people.png")
        self.top_image_label = Label(self.top, image=self.top_image, bg="#2378e8")
        self.top_image_label.place(x=130, y=20)

        self.heading = Label(self.top, text="Update Person",
                             font="arial 15 bold", bg="#2378e8", fg="#b1eb34")
        self.heading.place(x=230, y=50)
        # name entry code atart

        self.label_mane = Label(self.bottom, text="First Name", font="arial 15 bold", fg="white", bg="#9923e8")
        self.label_mane.place(x=40, y=40)

        self.entry_name = Entry(self.bottom, width=60, bd=4)
        self.entry_name.insert(0, person_name)
        self.entry_name.place(x=150, y=40)

        # surname
        self.label_surmane = Label(self.bottom, text="Surname", font="arial 15 bold", fg="white", bg="#9923e8")
        self.label_surmane.place(x=40, y=80)

        self.entry_surname = Entry(self.bottom, width=60, bd=4)
        self.entry_surname.insert(0, person_surname)
        self.entry_surname.place(x=150, y=80)
        # Email=======================================================
        self.label_email = Label(self.bottom, text="Email", font="arial 15 bold", fg="white", bg="#9923e8")
        self.label_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=60, bd=4)
        self.entry_email.insert(0, person_email)
        self.entry_email.place(x=150, y=120)
        # phone'======================================================
        self.label_phone = Label(self.bottom, text="Phone No", font="arial 15 bold", fg="white", bg="#9923e8")
        self.label_phone.place(x=40, y=160)

        self.entry_phone = Entry(self.bottom, width=60, bd=4)
        self.entry_phone.insert(0, person_phone)
        self.entry_phone.place(x=150, y=160)

        # Address ====================================================

        self.label_address = Label(self.bottom, text="Address", font="arial 15 bold", fg="white", bg="#9923e8")
        self.label_address.place(x=40, y=200)

        self.entry_address = Text(self.bottom, width=46, height=12)
        self.entry_address.insert(1.0, person_address)
        self.entry_address.place(x=150, y=200)

        # Buttons==============================================================
        button = Button(self.bottom, text="Update Data", font="arial 15 bold",
                        bg="#047d20", fg="#ebeef2", command=self.update_people)
        button.place(x=280, y=420)

    def update_people(self):
        id = self.person_id
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get(1.0, 'end-1c')
        query = "update addressbook set person_name = '{}', person_surname = '{}', person_email = '{}', person_phone = '{}', person_address = '{}' where person_id = {}". format(name, surname, email, phone, address, id)
        try:
            cur.execute(query)
            con.commit()
            messagebox.showinfo("Success", "Update Data")
        except Exception as e:
            print(e)



