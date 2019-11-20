from tkinter import *
import sqlite3
from addpeople import AddPeople
from updatepeople import Update
from display import Display
from tkinter import messagebox





con = sqlite3.connect('database.db')
cur = con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel. __init__(self)

        self.geometry("650x650+600+200")
        self.iconbitmap(r"icons.ico")
        self.title("My People")
        self.resizable(False,False)
        self.top = Frame(self, height=150, bg='#8c2d89')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#34c0eb")
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file="people.png")
        self.top_image_label = Label(self.top, image=self.top_image, bg="#8c2d89")
        self.top_image_label.place(x=130, y=20)

        self.heading = Label(self.top, text="My People",
                             font="arial 15 bold", bg="#8c2d89", fg="#b1eb34")
        self.heading.place(x=230, y=50)

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        self.listBox = Listbox(self.bottom, width=40, height=27)
        self.listBox.grid(row=0, column=0, padx=(40,0))
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        person = cur.execute("select * from 'addressbook'").fetchall()
        print(person)
        count = 0
        for person in person:
            self.listBox.insert(count, str(person[0])+ ". " +person[1]+" "+person[2])
            count += 1

        self.scroll.grid(row=0, column=1, sticky=N + S)

        #Buttons.................========================
        btnadd = Button(self.bottom, text="Add", width=12, font="sans 12 bold", command=self.add_people)
        btnadd.grid(row=0, column=2, padx=20, pady=10, sticky=N)

        btnUpdate = Button(self.bottom, text="Update", width=12, font="sans 12 bold",
                           command=self.update_function)
        btnUpdate.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        btnDisplay = Button(self.bottom, text="Display", width=12, font="sans 12 bold", command=self.display_function)
        btnDisplay.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        btnDelete = Button(self.bottom, text="Delete", width=12, font="sans 12 bold", command=self.delete_function)
        btnDelete.grid(row=0, column=2, padx=20, pady=130, sticky=N)

    def delete_function(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        query = "delete from addressbook where person_id = {}" .format(person_id)
        string_for_mbox = "Are You Sure You Wanna Delete", person.split(".")[1], "?"
        answer = messagebox.askquestion("Warning", "Are You Sure You Wanna Delete ?")
        if answer == 'yes':
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("Success", "Deleted Data")
                self.destroy()
            except Exception as e:
                messagebox.showinfo("Info", str(e))



    def add_people(self):
        add_page = AddPeople()
        self.destroy()
    def update_function(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        updatepage = Update(person_id)


    def display_function(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        displaypage = Display(person_id)
