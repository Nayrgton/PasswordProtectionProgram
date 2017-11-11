## @file PPP.py
# @author Suhavi Sandhu
# @brief The graphical user interface for a password manager
# @date November 10, 2017

from tkinter import *
from tkinter import ttk
import re
import database
import PWChecking
from Constants import *
import inactivity

## @brief An ADT that represents the GUI
class PPP(Tk):

    ## @brief PPP constructor
    #  @details Initializes a PPP GUI object using a variable argument list
    #  @param *args A variable argument list that contains information that should be dsplayed in GUI
    def __init__(self, *args):

        # Initialize GUI
        Tk.__init__(self, *args)        
        # Customizing window title, size and icon
        self.title("Password Protection Program")
        self.geometry(screen_size)
        self.configure(background=BGC)
        # self.wm_iconbitmap('logo.ico')
        # List of accounts
        self.accounts = []
        # Image of eye on button
        self.img = PhotoImage(file=eye)

        # Checks if master password has been initialized or not
        db = database.Account.select()
        if (len(db) == 0):
            self.showCreateMP()
        else:
            self.showLogIn()
        

    ## @brief Log In Screen
    #  @details Displays the log in frame
    def showLogIn(self):
        # Creating and adding the frame
        logIn = Frame(self, bg=BGC)      
        welcome = Label(logIn, text="Welcome to the Password Protection Program", fg=BG, bg=BGC, font=LARGE)
        welcome.grid(row=0, columnspan=3, padx=10, pady=10) # Divides space into 3 columns and places label in the middle
        enterLabel = Label(logIn, fg=BG, bg=BGC, text="Enter your master password")
        enterLabel.grid(row=1, column=1, padx=10, pady=2)
        ent = ttk.Entry(logIn, width=10, font=LARGE, show="*")
        ent.grid(row=2, column=1, padx=10, pady=10)
        # Allows submit button to work when the user presses Enter key and calls matchPassword method
        ent.bind('<Return>', lambda x: self.matchPassword(logIn, label=match, entry=ent))
        ent.focus_set()
        # When clicked, matchPassword method gets called with the frame name, label and the password entered by user
        btn = Button(logIn, text="Submit", fg=FG, bg=BG, font=LARGE, command=lambda: self.matchPassword(logIn, label=match, entry=ent))
        btn.grid(row=3, column=1)
        # Label that shows if the password matches the one in the database
        match = Label(logIn, fg=BG, bg=BGC, text="")
        match.grid(row=4, column=1)
        logIn.pack(expand=1)

    ## @brief Match Password
    #  @details Checks if password matches master password stored in database
    #  @param frame The frame which called the method, so it can be updated to show something else upon entering the correct password
    #  @param **kwargs A variable argument list, in this case takes the label that tells you if incorrect password and entry from user
    def matchPassword(self, frame, **kwargs):
        password = kwargs['entry'].get()
        # Get master password from DB and decrypt it
        mp = database.GetId(1).HashVal
        # Password checking
        response = PWChecking.checkLogIn(password, mp)
        # Makes sure the user entered the correct password
        if type(response) == str:
            kwargs['label'].config(text=response) # Updates label with correct resposne
        else:
            # Destroy the current frame, createMP
            frame.destroy()
            # Show the password mangement page
            self.showPWPage()
            self.configure(background=BG)
            return

    ## @brief Master Password Creation Screen
    #  @details Displays the master password creation frame
    def showCreateMP(self):
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
        btn = Button(createMP, text="Submit", command=lambda: self.checkMP(createMP, label=criteria, entry=ent))
        btn.grid(row=3, column=1)

        # Empty label that gets updated to show whether the password is strong enough
        criteria = Label(createMP, text="")
        criteria.grid(row=4, column=1)

        
    ## @brief Check Master Password
    #  @details Checks if password meets criteria for master password creation
    #  @param frame The frame which called the method, so it can be updated to show something else upon entering a satisfatory password
    #  @param **kwargs A variable argument list, in this case takes the label that tells you if incorrect password and entry from user
    def checkMP(self, frame, **kwargs):
        # Get password
        password = kwargs['entry'].get()
        response = PWChecking.checkMP(password)
        # If response is string, that means something is wrong with the input (not long enough, etc)
        if type(response) == str:
            # Updates label with correct response
            kwargs['label'].config(text=response)
        # Password satisfies constraints    
        else:
            # Call encryption methods
            enV, enK = password, "Encrypting"           
            # Insert to database method
            database.Insert(1, "Master", "Master", "", enV, enK)
            # Destroy the current frame, createMP
            frame.destroy()
            # Show the password mangement page
            self.showPWPage()
            return
        
    ## @brief Show entry
    #  @details Shows entries that already exists as a button on the left scrolling frame
    #  @param frame The frame that displays button
    #  @param detailFrame The frame that will show further details if button on left frame is clicked
    def showEntry(self, frame, detailFrame):
        i = 1
        # Check if database is empty
        if database.Account.table_exists():
            entries = database.Account.select()
        for entry in entries:
            # Get name of entries
            name = entry.AccName[:6]
            btn = Button(frame, text="\t"+name+"\t", image=self.img, compound="right", fg=FG,bg=BG, font=LARGE, anchor="w", command=lambda i=i: self.viewDetails(i,detailFrame))
            btn.config(height=75, width=60)
            btn.grid(row=7+i,columnspan=6, sticky=N+S+E+W)
            self.accounts.append(name)
            i+=1

        
    ## @brief Password Management Screen
    #  @details Where user can add and view account information
    #  @param *args A variable argument list
    def showPWPage(self, *args):

        ## @brief Updates scroll region when all widgets are in canvas
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox('all'))

        # Create beautiful canvas im picasso
        canvas = Canvas(self, bg=BG)
        canvas.pack(side=LEFT, fill='y')
        
        # Create scrollbar
        scrollbar = Scrollbar(self, command=canvas.yview, bg=BG)
        scrollbar.pack(side=LEFT, fill='y')

        # Attach scroll bar to canvas
        canvas.configure(yscrollcommand = scrollbar.set)

        # update scroll region
        canvas.bind('<Configure>', on_configure)

        # Add PWPage frame to canvas
        PWPage = Frame(canvas, bg=BG)
        canvas.create_window((0,0), window=PWPage, anchor='nw')

        # Add widgets
        instructions = Label(PWPage, bg=BG, fg=FG, text="Enter relevent information")
        instructions.grid(row=0, columnspan=2)
        nameL = Label(PWPage, bg=BG, fg=FG, font=LARGE, text="Account Name")
        nameE = ttk.Entry(PWPage, font=LARGE, width=10)
        typeL = Label(PWPage, bg=BG, fg=FG, font=LARGE, text="Account Type")
        typeE = ttk.Entry(PWPage, font=LARGE, width=10)
        userL = Label(PWPage, bg=BG, fg=FG, font=LARGE, text="Username")
        userE = ttk.Entry(PWPage, font=LARGE, width=10)
        passL = Label(PWPage, bg=BG, fg=FG, font=LARGE, text="Password")
        passE = ttk.Entry(PWPage, font=LARGE, width=10)
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
        btn = Button(PWPage, text="Submit", bg=BGC, fg=BG, font=LARGE, command=lambda: self.addEntry(PWPage, detailFrame, canvas, nameE, typeE, userE, passE))
        btn.grid(row=5, column=1, padx=5, pady=10)

        # Frame for showing details
        detailFrame = Frame(self)
        detailFrame.pack()

        # Show existing entries
        self.showEntry(PWPage, detailFrame)


    ## @brief Add entry to database and display in scrollbar frame
    #  @details Adds entry to the database and the display
    #  @param scrollFrame The frame on the left which displays the entries as buttons
    #  @param detailFrame The frame on the right which displays details of each entry
    #  @param *pwd Variable list of entries from the user when he/she adds an entry
    def addEntry(self, scrollFrame, canvas, detailFrame, *pwd):
        AccName = pwd[0].get() # The account name
        AccType = pwd[1].get() # The account type
        UserName = pwd[2].get() # The username for the account
        Password = pwd[3].get() # Password for the account
        
        # Hash key as generated by encryption module
        HashKey = "Encrypted!"

        # Add entry to list
        self.accounts.append(AccName)

        # Add entry to database
        database.Insert(len(self.accounts), AccName, AccType, UserName, Password, HashKey)

        # ID of entry to denote where to place each entry on the scrollframe
        i = len(self.accounts)
        # Creates a button for the entry at the appropriate position
        viewBtn = Button(scrollFrame, text="\t"+AccName+"\t", image=self.img, compound="right", fg=FG, bg=BG, font=LARGE, anchor="w", command=lambda i=i: self.viewDetails(i, detailFrame))
        viewBtn.config(height=75, width=60)
        viewBtn.grid(row=7+i, columnspan=6, sticky=N+S+E+W)


    ## @brief Displays details of entry
    #  @details Displays details of entry (type, name, username, password), called when button for entry is clicked
    #  @param idnum The id number of the entry that was clicked
    #  @param frame The frame in which to display the details on
    def viewDetails(self, idnum, frame):
        # Get full entry from database
        query = database.GetId(idnum)
        # Delete everything in frame currently
        for widget in frame.winfo_children():
            widget.destroy()
        # Add new details
        namelabel = Label(frame, text=query.AccName)
        namelabel.pack()
        typelabel = Label(frame, text=query.AccType)
        typelabel.pack()
        Userlabel = Label(frame, text=query.UserName)
        Userlabel.pack()
        passlabel = Label(frame, text=query.HashVal)
        passlabel.pack()
        
   
# Runs application
app = PPP()
app.mainloop()
