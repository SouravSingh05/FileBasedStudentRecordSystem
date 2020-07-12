from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.resizable(0, 0)
        self.root.title("Login")
        self.root.geometry("600x470+400+100")  # setting width and height and giving x and y coordinate
        self.bg_icon = ImageTk.PhotoImage(file="bg.jpg")
        bg_lbl = Label(self.root, image=self.bg_icon)
        bg_lbl.pack()
        self.icon = ImageTk.PhotoImage(file="icon.jpg")
        title = Label(self.root, text="Login", font=("times new roman", 30, "bold"), bg="#48BF91")
        title.place(x=0, y=0, relwidth=1)
        bg_lbl = Label(self.root, image=self.bg_icon)
        bg_lbl.pack()
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=120, y=100)
        logo = Label(login_frame, image=self.icon)
        logo.grid(row=0, column=0, columnspan=2)
        user = Label(login_frame, text="User Name", bg="white", font=("", 15))
        user.grid(row=1, column=0, padx=5, pady=5)
        self.uname = StringVar()
        userentry = Entry(login_frame, bg="white", textvariable=self.uname, font=("", 15))
        userentry.grid(row=1, column=1, padx=5, pady=5)
        password = Label(login_frame, text="Password", bg="white", font=("", 15))
        password.grid(row=2, column=0, padx=5, pady=5)
        self.passw = StringVar()
        passentry = Entry(login_frame, bg="white", show="*", textvariable=self.passw, font=("", 15))
        passentry.grid(row=2, column=1, padx=5, pady=5)
        submit = Button(login_frame, text="Login", width=10, bg="#48BF91", command=self.login)
        submit.grid(row=3, column=0, padx=5, pady=5)
        reset = Button(login_frame, text="Reset", width=10, bg="#48BF91", command=self.reset)
        reset.grid(row=3, column=1, padx=5, pady=5)

    def login(self):
        if self.uname.get() == "" or self.passw.get() == "":
            messagebox.showerror("Error", "All fields are required!!")
        elif self.uname.get() == "Sourav" and self.passw.get() == "Sourav123":
            messagebox.showinfo("Login", f"Welcome {self.uname.get()}")
            self.root.destroy()
            import FilebasedRecordSystem
            FilebasedRecordSystem.FileApp()
        else:
            messagebox.showerror("Error", "Wrong User Name and password combination")

    def reset(self):
        self.uname.set("")
        self.passw.set("")


root = Tk()
obj = LoginSystem(root)
root.mainloop()