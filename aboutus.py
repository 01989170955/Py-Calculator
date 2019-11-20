from tkinter import *

class About(Toplevel):
    def __init__(self):
        Toplevel. __init__(self)

        self.geometry("550x550+550+200")
        self.iconbitmap(r"icons.ico")
        self.title("About Us")
        self.resizable(False,False)

        self.top = Frame(self, height=550, bg='#3e65f0')
        self.top.pack(fill=BOTH)

        self.text = Label(self.top, text="Md. Al Amin Sarkar.\n Student Of Sherpur Polytechnic Institute.\n Future Computer Programe Developer.\nEmail: bm15.telecom@gmail.com\n Phone: 01989-170955",
                         font="arial 15 bold", bg="#3e65f0", fg="white")
        self.text.place(x=50, y=50)
