## @file PPP.py
# @author Tuples1
# @brief The graphical user interface for a password manager
# @date October 30, 2017

from tkinter import *
from tkinter import ttk
import re


# Background colour
BGC = "#E6E6FA"

# Large font
LARGE = ("Helvetica", 16)


## @brief An ADT that represents the GUI
class PPP(Tk):

    ## @brief PPP constructor
    #  @details Initializes a PPP GUI object using a variable argument list
    #  @param *args A variable argument list that contains information that should be dsplayed in GUI
    def __init__(self, *args):

        # Initialize GUI
        Tk.__init__(self, *args)

        # States of the GUI that are used in multiple methods
        self.state = {
            "prompt": "Enter your master password", "val": False
            }

        
        self.showLogIn()
        # Checks if master password has been initialized or not
        '''
        if (password in database):
            self.showLogIn()
        else:
            self.showCreateMP()
        '''

        # Customizing window title, size and icon
        self.title("Password Protection Program")
        self.geometry("1080x840")
        # self.wm_iconbitmap('logo.ico')

    ## @brief Log In Screen
    #  @details DIsplays the log in frame
    #  @param *kwargs A variable argument list to provide extra functionality to the frame
    def showLogIn(self, *kwargs):

        # Creatiing and adding the frame
        logIn = Frame(self)
        logIn.pack()
        
        welcome = Label(logIn, text="Welcome to the Password Protection Program", font=LARGE)
        welcome.grid(row=0, columnspan=3) # Divides space into 3 columns and places label in the middle

        enterLabel = Label(logIn, text=self.state['prompt'])
        enterLabel.grid(row=1, column=1)

        ent = ttk.Entry(logIn, show="*")
        ent.grid(row=2, column=1)

        # Allows submit button to work when the user presses Enter key and calls matchPassword method
        ent.bind('<Return>', lambda x: self.matchPassword(logIn, label=match, entry=ent))
        ent.focus_set()

        # When clicked, matchPassword method gets called with the frame name, label and the password entered by user
        btn = Button(logIn, text="Submit", command=lambda: self.matchPassword(logIn, label=match, entry=ent))
        btn.grid(row=3, column=1)

        # Label that shows if the password matches the one in the database
        match = Label(logIn, text="")
        match.grid(row=4, column=1)

    ## @brief Match Password
    #  @details Checks if password matches master password stored in database
    #  @param frame The frame which called the method, so it can be updated to show something else upon entering the correct password
    #  @param **kwargs A variable argument list, in this case takes the label that tells you if incorrect password and entry from user
    def matchPassword(self, frame, **kwargs):
        password = kwargs['entry'].get()

        # Get master password from DB
        # Unencrypt it
        # Master password from DB
        mp = "Assssss1"

        # Makes sure the user entered the correct password
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

        # Updates label with correct resposne
        kwargs['label'].config(text=msg)

    ## @brief Master Password Creation Screen
    #  @details Displays the master password creation frame
    #  @param *kwargs A variable argument list to provide extra functionality to the frame
    def showCreateMP(self, *args):

        # Similarly to showLogIn method, creates and adds widgets to frame
        createMP = Frame(self)
        createMP.pack()

        welcome = Label(createMP, text="Welcome to the Password Protection Program", font=LARGE)
        welcome.grid(row=0, columnspan=3)

        enterLabel = Label(createMP, text="Create a master password to start using the application")
        enterLabel.grid(row=1, column=1)

        ent = ttk.Entry(createMP, show="*")
        ent.grid(row=2, column=1)
        ent.bind('<Return>', lambda x: self.checkPassword(createMP, label=criteria, entry=ent))
        ent.focus_set() # sets focus to entry box

        # When clicked, matchPassword method gets called with the frame name, label and the password entered by user
        btn = Button(createMP, text="Submit", command=lambda: self.checkPassword(createMP, label=criteria, entry=ent))
        btn.grid(row=3, column=1)

        # Empty label that gets updated to show whether the password is strong enough
        criteria = Label(createMP, text="")
        criteria.grid(row=4, column=1)

        
    ## @brief Check Password
    #  @details Checks if password meets criteria for master password creation
    #  @param frame The frame which called the method, so it can be updated to show something else upon entering a satisfatory password
    #  @param **kwargs A variable argument list, in this case takes the label that tells you if incorrect password and entry from user
    def checkPassword(self, frame, **kwargs):
        # Get password
        password = kwargs['entry'].get()
    
        if len(password) == 0:
            msg = "Password cannot be empty"

        elif len(password) < 8:
            msg = "Password must be at least 8 characters"

        elif not(re.search("[0-9]", password)):
            msg = "Password must have at least 1 number"
            
        elif not(re.search("[a-z]", password) and re.search("[A-Z]", password)):
            msg = "Password must have uppercase and lowercase"

        # Password satisfies constraints    
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

        # Updates label with correct response
        kwargs['label'].config(text=msg)


    def showPWPage(self, *args):
        PWPage = Frame(self)
        PWPage.pack()

        w = Label(PWPage, text="smd")
        w.grid(row=0, columnspan=3)
        
            
# Runs application
app = PPP()
app.mainloop()
            
        






