from  tkinter import  *
import  datetime
from mypeople import MyPeople
from addpeople import AddPeople
from aboutus import About

date = datetime.datetime.now().date()
date = str(date)


class Application(object):
    def __init__(self, master):
        self.master = master
# frame ====================================================
        self.top = Frame(master, height=150, bg='Gray')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg="#7842f5")
        self.bottom.pack(fill=X)

        self.top_image = PhotoImage(file="icons.png")
        self.top_image_label = Label(self.top, image=self.top_image, bg="Gray")
        self.top_image_label.place(x=130, y=20)

        self.heading = Label(self.top, text="My Phonebook App",
                             font="arial 15 bold", bg="Gray", fg="#b1eb34")
        self.heading.place(x=230, y=50)
        self.date_lbl = Label(self.top, text="Today's date: "+date, font="arial 12 bold",
                              fg="#b1eb34", bg="Gray")
        self.date_lbl.place(x=450, y=110)

        # button adding line start___________________________________________

        self.viewButton = Button(self.bottom, text="  My People  ", bg="#bdeb34", font="arial 12 bold", command=self.my_people)
        self.viewButton.place(x=270, y=70)

        self.addButton = Button(self.bottom, text=" Add People ", bg="#bdeb34", font="arial 12 bold", command=self.addpeoplefunction)
        self.addButton.place(x=270, y=130)

        self.aboutButton = Button(self.bottom, text="   About Us   ", bg="#bdeb34", font="arial 12 bold", command=self.about_us)
        self.aboutButton.place(x=270, y=190)

    def my_people(self):
        people = MyPeople()

    def about_us(self):
        pass

    def addpeoplefunction(self):
        addpeoplewindow = AddPeople()

    def about_us(self):
        aboutpage = About()



#=============================================================




def main():
    root = Tk()
    app = Application(root)
    root.title("Phonebook App")
    root.geometry("650x550+350+200")
    root.iconbitmap(r"icons.ico")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()
