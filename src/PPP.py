from tkinter import *
from tkinter import ttk
import re

bgc = "#E6E6FA"
LARGE = ("Helvetica", 16)
BUTTONS = ("Sans-Serif", 10, "bold")


# Class for the GUI wi
class PPP(Tk):

    def __init__(self, *args):
        Tk.__init__(self, *args)

        self.state = {
            "prompt": "Enter your master password", "val": False
            }

        self.showLogIn()
        '''
        if (password in database):
            self.showLogIn()
        else:
            self.showCreateMP()
        '''    
        self.title("Password Protection Program")
        self.geometry("1080x840")
        # window.wm_iconbitmap('logo.ico')

    # Show appropriate fram
    def showLogIn(self, *kwargs):
        logIn = Frame(self)
        logIn.pack()

        welcome = Label(logIn, text="Welcome to the Password Protection Program", font=LARGE)
        welcome.grid(row=0, columnspan=3)

        enterLabel = Label(logIn, text=self.state['prompt'])
        enterLabel.grid(row=1, column=1)

        ent = ttk.Entry(logIn, show="*")
        ent.grid(row=2, column=1)
        ent.bind('<Return>', lambda x: self.matchPassword(logIn, label=criteria, entry=ent, btn=btn))
        ent.focus_set()

        btn = Button(logIn, text="Submit", command=lambda: self.matchPassword(logIn, label=criteria, entry=ent, btn=btn))
        btn.grid(row=3, column=1)
        
        criteria = Label(logIn, text="")
        criteria.grid(row=4, column=1)

    # Checks if password is good and then encrypts it to a file, additional parameters enterLabel, entry and button
    def matchPassword(self, frame, **kwargs):
        password = kwargs['entry'].get()

        # Get master password from DB
        # Unencrypt it
        mp = "Assssss1"

        if len(password) == 0:
            msg = "Password cannot be empty"

        elif password != mp:
            msg = "Incorrect password"

        elif password == mp:
            # Destroy the current frame, createMP
            frame.destroy()
            # Show the password mangement page
            self.showPWPage()
            return

        kwargs['label'].config(text=msg)

    # Checks if password is good and then encrypts it to a file, additional parameters enterLabel, entry and button
    def checkPassword(self, frame, **kwargs):
        password = kwargs['entry'].get()

        if len(password) == 0:
            msg = "Password cannot be empty"

        elif len(password) < 8:
            msg = "Password must be at least 8 characters"

        elif not(re.search("[0-9]", password)):
            msg = "Password must have at least 1 number"
            
        elif not(re.search("[a-z]", password) and re.search("[A-Z]", password)):
            msg = "Password must have uppercase and lowercase"
            
        else:
            # Call encryption methods
            print("Encrypting")
            # Insert to database method
            print("Inserting to database")
            # Destroy the current frame, createMP
            frame.destroy()
            # Show the password mangement page
            self.showPWPage()
            return

        kwargs['label'].config(text=msg)

    def showCreateMP(self, *args):
        createMP = Frame(self)
        createMP.pack()

        welcome = Label(createMP, text="Welcome to the Password Protection Program", font=LARGE)
        welcome.grid(row=0, columnspan=3)

        enterLabel = Label(createMP, text="Create a master password to start using the application")
        enterLabel.grid(row=1, column=1)

        ent = ttk.Entry(createMP, show="*")
        ent.grid(row=2, column=1)
        ent.bind('<Return>', lambda x: self.checkPassword(createMP, label=criteria, entry=ent, btn=btn))
        ent.focus_set() # sets focus to entry box

        btn = Button(createMP, text="Submit", command=lambda: self.checkPassword(createMP, label=criteria, entry=ent, btn=btn))
        btn.grid(row=3, column=1)
        
        criteria = Label(createMP, text="")
        criteria.grid(row=4, column=1)

    def showPWPage(self, *args):
        PWPage = Frame(self)
        PWPage.pack()

        w = Label(PWPage, text="smd")
        w.grid(row=0, columnspan=3)
        

class HomeScreen(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # Welcome label
        welcome = Label(self, text="Welcome to the Password Protection Program", bg=bgc, font=("Helvetica",16))
        welcome.pack(pady=10,padx=10)

        enterLabel = Label(self, text="Enter a master password to keep all your usernames and passwords secure")
        enterLabel.pack()

        # Enter password
        ent = Entry(self, show="*")
        ent.pack()

       
        
        # Button
        btn = Button(self, text="Enter", font=("Helvetica",16), command=checkPassword)
        btn.pack()

        # Password strength
        mesg = Label(self, text="", bg=bgc)
        mesg.pack()

        welcome.place(relx=.5, rely=.3, anchor="c")
        enterLabel.place(relx=.5, rely=.45, anchor="c")
        ent.place(relx=.5, rely=.5, anchor="c")
        btn.place(relx=.5, rely=.55, anchor="c")
        mesg.place(relx=.5, rely=.6, anchor="c")


        
class PWPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        welcome = Label(self, text="Add an entry to the PasswordPotatoProgram", bg=bgc, font=("Helvetica",16))
        welcome.pack(pady=10,padx=10)


        nameLabel = Label(self, text="Name")
        nameLabel.pack()
        
        typeLabel = Label(self, text="Type")
        typeLabel.pack()

        typeEnt = Entry(self)
        typeEnt.pack()

        userLabel = Label(self, text="Username")
        userLabel.pack()

        userEnt = Entry(self)
        userEnt.pack()

        passLabel = Label(self, text="Password")
        passLabel.pack()

        passEnt = Entry(self, show="*")
        passEnt.pack()

        addButton = Button(self, text="Add")
        addButton.pack()


                

            

app = PPP()

app.mainloop()
            
        






