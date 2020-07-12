from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os


class FileApp():
    def __init__(self):
        self.root = Tk()
        self.root.title("File Based Record System")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(0, 0)
        title = Label(self.root, text="File Based Record System", font=("algerian", 30))
        title.place(x=0, y=10, relwidth=1)

# creating frame for writing details======================================================================

        studentdetail = Frame(self.root, bd=4, relief=GROOVE, bg="#48BF91")
        studentdetail.place(x=50, y=70, width=750, height=500)
        stitle = Label(studentdetail, text="Student Details", font=("algerian", 25), bg="#48BF91")
        stitle.grid(row=0, columnspan=4, pady=10)

        sid = Label(studentdetail, text="Student ID", font=("algerian", 15), bg="#48BF91")
        sid.grid(row=1, column=0, padx=10, pady=20, sticky="w")
        self.siden = StringVar()
        side = Entry(studentdetail, textvariable=self.siden, font=("", 13))
        side.grid(row=1, column=1, padx=10, pady=20)

        con = Label(studentdetail, text="Contact No", font=("algerian", 15), bg="#48BF91")
        con.grid(row=1, column=2, padx=10, pady=20, sticky="w")
        self.conen = StringVar()
        cone = Entry(studentdetail, textvariable=self.conen, font=("", 13))
        cone.grid(row=1, column=3, padx=10, pady=20)

        name = Label(studentdetail, text="Name", font=("algerian", 15), bg="#48BF91")
        name.grid(row=2, column=0, padx=10, pady=20, sticky="w")
        self.nameen = StringVar()
        namee = Entry(studentdetail, textvariable=self.nameen, font=("", 13))
        namee.grid(row=2, column=1, padx=10, pady=20)

        date = Label(studentdetail, text="Date", font=("algerian", 15), bg="#48BF91")
        date.grid(row=2, column=2, padx=10, pady=20, sticky="w")
        self.dateen = StringVar()
        datee = Entry(studentdetail, textvariable=self.dateen, font=("", 13))
        datee.grid(row=2, column=3, padx=10, pady=20)

        course = Label(studentdetail, text="Course", font=("algerian", 15), bg="#48BF91")
        course.grid(row=3, column=0, padx=10, pady=20, sticky="w")
        self.courseen = StringVar()
        coursee = ttk.Combobox(studentdetail, font=("", 11), state="readonly", textvariable=self.courseen)
        coursee['values'] = ("BTech", "MTech", "BBA", "MBA", "BSc", "MSc")
        coursee.grid(row=3, column=1, padx=10, pady=20)

        degree = Label(studentdetail, text="Degree", font=("algerian", 15), bg="#48BF91")
        degree.grid(row=3, column=2, padx=10, pady=20, sticky="w")
        self.degreeen = StringVar()
        degreee = ttk.Combobox(studentdetail, font=("", 11), state="readonly", textvariable=self.degreeen)
        # stopping the user to write in combobox
        degreee['values'] = ("Undergraduate", "Post Graduate")  # giving values to combobox
        degreee.grid(row=3, column=3, padx=10, pady=20)

        add = Label(studentdetail, text="Address", font=("algerian", 15), bg="#48BF91")
        add.grid(row=4, column=0, padx=10, pady=20, sticky="w")
        self.adden = StringVar()
        adde = Entry(studentdetail, textvariable=self.adden, font=("", 13))
        adde.grid(row=4, column=1, padx=10, pady=20)

        id = Label(studentdetail, text="ID Proof", font=("algerian", 15), bg="#48BF91")
        id.grid(row=4, column=2, padx=10, pady=20, sticky="w")
        self.iden = StringVar()
        ide = ttk.Combobox(studentdetail, font=("", 11), state="readonly", textvariable=self.iden)
        # stopping the user to write in combobox
        ide['values'] = ("Passport", "Pan Card", "Adhaar Card", "Voter Card")  # giving values to combobox
        ide.grid(row=4, column=3, padx=10, pady=20)

        city = Label(studentdetail, text="City", font=("algerian", 15), bg="#48BF91")
        city.grid(row=5, column=0, padx=10, pady=20, sticky="w")
        self.cityen = StringVar()
        citee = Entry(studentdetail, textvariable=self.cityen, font=("", 13))
        citee.grid(row=5, column=1, padx=10, pady=20)

        pay = Label(studentdetail, text="Payment", font=("algerian", 15), bg="#48BF91")
        pay.grid(row=5, column=2, padx=10, pady=20, sticky="w")
        self.payen = StringVar()
        paye = ttk.Combobox(studentdetail, font=("", 11), state="readonly", textvariable=self.payen)
        # stopping the user to write in combobox
        paye['values'] = ("Cash", "Card", "Cheque", "DD", "Internet Banking")  # giving values to combobox
        paye.grid(row=5, column=3, padx=10, pady=20)

# creating frame for buttons==============================================================================

        button = Frame(self.root, bd=4, relief=GROOVE, bg="#48BF91")
        button.place(x=50, y=590, width=750, height=80)

        add = Button(button, text="Add", width=15, bg="gray", font=("algerian", 10), command=self.update)
        add.grid(row=0, column=0, padx=10, pady=15, ipady=5, sticky="w")

        delete = Button(button, text="Delete", width=15, bg="gray", font=("algerian", 10), command=self.delete)
        delete.grid(row=0, column=1, padx=10, pady=15, ipady=5, sticky="w")

        clear = Button(button, text="Clear", width=15, bg="gray", font=("algerian", 10), command=self.clear)
        clear.grid(row=0, column=2, padx=10, pady=15, ipady=5, sticky="w")

        logout = Button(button, text="Logout", width=15, bg="gray", font=("algerian", 10), command=self.logout)
        logout.grid(row=0, column=3, padx=10, pady=15, ipady=5, sticky="w")

        exit = Button(button, text="Exit", width=14, bg="gray", font=("algerian", 10), command=self.exit)
        exit.grid(row=0, column=4, padx=10, pady=15, ipady=5, sticky="w")

# creating frame for displaying files=====================================================================

        file = Frame(self.root, bd=4, relief=GROOVE, bg="#48BF91")
        file.place(x=850, y=70, width=445, height=600)
        ftitle = Label(file, text="All Files", font=("algerian", 25), bg="#48BF91", bd=4, relief=GROOVE)
        ftitle.pack(side=TOP, fill=X)
        scrolly = Scrollbar(file, orient=VERTICAL)
        self.filelist= Listbox(file, yscrollcommand=scrolly.set, bg="#D3D3D3")
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.filelist.yview)
        self.filelist.pack(fill=BOTH, expand=1)
        self.filelist.bind("<ButtonRelease-1>", self.get)
        self.show()
        self.root.mainloop()
    def update(self):
        f = os.listdir("files/")
        present = "no"
        for i in f:
            v = i.split(".")
            if v[0] == self.siden.get():
                present = "yes"
        if present == "yes":
            ask = messagebox.askyesno("Update", "File already present.\nDo you want to update the records?")
            if ask == 1:
                self.add()
                messagebox.showinfo("Success", "Record has been updated")
        else:
            self.add()
            messagebox.showinfo("Success", "Record has been saved")

    def add(self):
        if self.siden.get() == "" or self.nameen.get() == "" or self.courseen.get() == "" or self.adden.get() == "" or \
                self.cityen.get() == "" or self.conen.get() == "" or self.dateen.get() == "" or self.degreeen.get() == \
                "" or self.iden.get() == "" or self.payen.get() == "":
            messagebox.showwarning("Warning", "All Fields Are Required")
        else:
            f = open("files/"+str(self.siden.get())+".txt", "w")  # opening a file w is for write only
            f.write(
                str(self.siden.get()) + "," +
                str(self.nameen.get()) + "," +
                str(self.courseen.get()) + "," +
                str(self.adden.get()) + "," +
                str(self.cityen.get()) + "," +
                str(self.conen.get()) + "," +
                str(self.dateen.get()) + "," +
                str(self.degreeen.get()) + "," +
                str(self.iden.get()) + "," +
                str(self.payen.get())
            )
            f.close()
            self.show()
            self.clear()

    def show(self):
        files = os.listdir("files/")
        self.filelist.delete(0, END)
        if len(files) > 0:
            for file in files:
                self.filelist.insert(END, file)

    def get(self, event):
        getcur = self.filelist.curselection()  # selecting the file from file list
        f1 = open("files/"+self.filelist.get(getcur))  # opening text file
        value = []
        for f in f1:
            value = f.split(",")
        self.siden.set(value[0])
        self.nameen.set(value[1])
        self.courseen.set(value[2])
        self.adden.set(value[3])
        self.cityen.set(value[4])
        self.conen.set(value[5])
        self.dateen.set(value[6])
        self.degreeen.set(value[7])
        self.iden.set(value[8])
        self.payen.set(value[9])

    def clear(self):
        self.siden.set("")
        self.nameen.set("")
        self.courseen.set("")
        self.adden.set("")
        self.cityen.set("")
        self.conen.set("")
        self.dateen.set("")
        self.degreeen.set("")
        self.iden.set("")
        self.payen.set("")

    def delete(self):
        present = "no"
        if self.siden.get() == "":
            messagebox.showwarning("Warning", "Student ID is Required")
        else:
            f = os.listdir("files/")
            if len(f) > 0:
                for i in f:
                    v = i.split(".")
                    if v[0] == self.siden.get():
                        present = "yes"
                if present == "yes":
                    ask = messagebox.askyesno("Delete", "Do you really want to delete?")
                    if ask == 1:  # in case of yes
                        os.remove("files/"+self.siden.get()+".txt")
                        messagebox.showinfo("Deleted", "Detail has been deleted.")
                        self.show()
                        self.clear()
                else:
                    messagebox.showwarning("Warning", "No Record Found")

    def exit(self):
        ask = messagebox.askyesno("Exit", "Do you really want to exit?")
        if ask == 1:
            self.root.destroy()

    def logout(self):
        self.root.destroy()
        import login
