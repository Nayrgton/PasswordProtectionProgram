## @file PPP.py
# @author Tuples1
# @brief The graphical user interface for a password manager
# @date October 30, 2017

from tkinter import *
from tkinter import ttk
import re
import database


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
        # List of accounts
        self.accounts = []


        ## JOSEPH -- TESTING REQUIRED ##
        # Checks if master password has been initialized or not
        db = database.Account.select()
        if (len(db)):
            self.showLogIn()
        else:
            self.showCreateMP()
        

        # Customizing window title, size and icon
        self.title("Password Protection Program")
        self.geometry("1080x840")
        # self.wm_iconbitmap('logo.ico')

    ## @brief Log In Screen
    #  @details Displays the log in frame
    #  @param *kwargs A variable argument list to provide extra functionality to the frame
    def showLogIn(self, *kwargs):

        # Creatiing and adding the frame
        logIn = Frame(self)
        logIn.pack()
        
        welcome = Label(logIn, text="Welcome to the Password Protection Program", font=LARGE)
        welcome.grid(row=0, columnspan=3, padx=10, pady=10) # Divides space into 3 columns and places label in the middle

        enterLabel = Label(logIn, text=self.state['prompt'])
        enterLabel.grid(row=1, column=1, padx=10, pady=10)

        ent = ttk.Entry(logIn, show="*")
        ent.grid(row=2, column=1, padx=10, pady=10)

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
        ## JOSEPH ##
        mp = database.GetId(1).HashVal # remember to change this when encryption works
        
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
            enV = password
            enK = "Encrypting"
            
            # Insert to database method
            ## JOSEPH ##
            database.Insert(1, "Master", "Master", "", enV, enK)

            # Destroy the current frame, createMP
            frame.destroy()
            # Show the password mangement page
            self.showPWPage()
            return

        # Updates label with correct response
        kwargs['label'].config(text=msg)
        
    def showEntry(self, frame, detailFrame):
        entries = []
        i = 0

        # Check if database is empty
        if database.Account.table_exists():
            
            # If it's not empty, display entries
            entries = database.Account.select()
            i = len(entries)

        for entry in entries:
            # Get name of entries
            name = entry.AccName
            btn = Button(frame, text=name, command=lambda i=i: self.viewDetails(i,detailFrame))
            btn.grid(row=7+i, column=1)
            self.accounts.append(name)
            i-=1

        
    ## @brief Password Management Screen
    #  @details Where user can add and view account information
    #  @param *args A variable argument list
    def showPWPage(self, *args):

        ## @brief Updates scroll region when all widgets are in canvas
        def on_configure(event):
            # update scrollregion after starting 'mainloop'
            # when all widgets are in canvas
            
            canvas.configure(scrollregion=canvas.bbox('all'))

        # Create beautiful canvas im picasso
        canvas = Canvas(self)
        canvas.pack(side=LEFT, fill='y')
        
        # Create scrollbar
        scrollbar = Scrollbar(self, command=canvas.yview)
        scrollbar.pack(side=LEFT, fill='y')

        # Attach scroll bar to canvas
        canvas.configure(yscrollcommand = scrollbar.set)

        # update scroll region
        canvas.bind('<Configure>', on_configure)

        # Add PWPage frame to canvas
        PWPage = Frame(canvas)
        canvas.create_window((0,0), window=PWPage, anchor='nw')

        # Add widgets
        instructions = Label(PWPage, text="Enter relevent information")
        instructions.grid(row=0, column=1)

        nameL = Label(PWPage, text="Account Name")
        nameE = ttk.Entry(PWPage)
        typeL = Label(PWPage, text="Account Type")
        typeE = ttk.Entry(PWPage)
        userL = Label(PWPage, text="Username")
        userE = ttk.Entry(PWPage)
        passL = Label(PWPage, text="Password")
        passE = ttk.Entry(PWPage)
        nameL.grid(row=1, column=0)
        nameE.grid(row=1, column=1)
        typeL.grid(row=2, column=0)
        typeE.grid(row=2, column=1)
        userL.grid(row=3, column=0)
        userE.grid(row=3, column=1)
        passL.grid(row=4, column=0)
        passE.grid(row=4, column=1)

        # Allows submit button to work when the user presses Enter key and calls addEntry method
        passE.bind('<Return>', lambda x: self.addEntry(PWPage, detailFrame, nameE, typeE, userE, passE))
        nameE.focus_set()

        # When clicked, addEntry method gets called with the frame name and relevant entries
        btn = Button(PWPage, text="Submit", command=lambda:  self.addEntry(PWPage, detailFrame, nameE, typeE, userE, passE))
        btn.grid(row=5, column=1)

        # Frame for showing details
        detailFrame = Frame(self)
        detailFrame.pack()

        # Show existing entries
        self.showEntry(PWPage, detailFrame)
        '''        
        # Show existing entries
        count_entries = 5
        for i in range(count_entries):
            # Get name of entries
            name = "Account"+str(i)
            self.accounts.append(name)
            # Get id of entry
            # change viewDetails 'i' to id
            btn = Button(PWPage, text=name, command=lambda i=i: self.viewDetails(i, detailFrame))
            btn.grid(row=7+i, column=1)
    '''
    ## @brief Add entry to database and display in scrollbar frame
    def addEntry(self, scrollFrame, detailFrame, *pwd):
        AccName = pwd[0].get()
        AccType = pwd[1].get()
        UserName = pwd[2].get()
        Password = pwd[3].get()
        # Add entries to database
        HashKey = "Encrypted!"

        # Add entry to list
        self.accounts.append(AccName)
        
        database.Insert(len(self.accounts), AccName, AccType, UserName, Password, HashKey)

        ## JOSEPH ##
        # Get id of entry
        # for now it's extracted from list
        i = len(self.accounts)

        viewBtn = Button(scrollFrame, text=AccName, command=lambda i=i: self.viewDetails(i, detailFrame))
        viewBtn.grid(row=7+i, column=1)


    def viewDetails(self, idnum, frame):
        # Get full entry from database
        #query, enPass = database.GetId(idnum)
        print(idnum)
        password = database.GetId(idnum).HashVal

        # Delete everything in frame currently
        for widget in frame.winfo_children():
            widget.destroy()

        #namelabel = Label(frame, text=query.AccName)
        #namelabel.pack()
        #typelabel = Label(frame, text=query.AccType)
        #tyoelabel.pack()
        #Userlabel = Label(frame, text=query.UserName)
        #Userlabel.pack()
        passlabel = Label(frame, text=password)
        passlabel.pack()
        
                        

                   
# Runs application
app = PPP()
app.mainloop()
