from tkinter import *
import re

bgc = "#E6E6FA"

class PPP(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomeScreen, PWPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomeScreen)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class HomeScreen(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # Welcome label
        welcome = Label(self, text="Welcome to the Password Protection Program", bg=bgc, font=("Helvetica",16))
        welcome.pack(pady=10,padx=10)

        # Enter password
        ent = Entry(self, show="*")
        ent.pack()

        # Checks if password is good and then encrypts it to a file
        def checkPassword():
            password = ent.get()
            strength = 0

            if len(password) == 0:
                msg = "Password cannot be empty"

            elif len(password) < 8:
                msg = "Password must be at least 8 characters"

            elif not(re.search("[0-9]", password)):
                msg = "Password must have at least 1 number"
                
            elif not(re.search("[a-z]", password) and re.search("[A-Z]", password)):
                msg = "Password must have uppercase and lowercase"
                
            else:
                controller.show_frame(PWPage)
                return

            mesg.configure(text=msg)
        
        # Button
        btn = Button(self, text="Enter", font=("Helvetica",16), command=checkPassword)
        btn.pack()

        # Password strength
        mesg = Label(self, text="", bg=bgc)
        mesg.pack()

        
class PWPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        welcome = Label(self, text="Add an entry to the PasswordPotatoProgram", bg=bgc, font=("Helvetica",16))
        welcome.pack(pady=10,padx=10)

        plus = Button(self, text="+", command=lambda: showEntry())
        plus.pack()

        def showEntry():
            typeLabel = Label(self, text="What type of account is this?")
            typeLabel.pack()

            typeEnt = Entry(self)
            typeEnt.pack()

            userLabel = Label(self, text="Username")
            userLabel.pack()

app = PPP()

app.mainloop()
            
        






